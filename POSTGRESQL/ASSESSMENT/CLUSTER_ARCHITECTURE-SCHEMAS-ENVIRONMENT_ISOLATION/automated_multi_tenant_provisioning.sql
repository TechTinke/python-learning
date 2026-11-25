-- Automated Multi-Tenant Provisioning & Privilege Containment
-- A B2B logistics startup is onboarding enterprise clients.
-- Under PostgreSQL's catalog architecture, database roles exist globally across an entire cluster, whereas schemas act as logical namespaces inside a single database.
-- If a connection defaults to the public schema in the search_path, a newly created role with CREATE privileges on public can hijack unqualified queries from other tenants.
-- Design the cluster role hierarchy, database connection parameters, and schema initialization pipeline so new clients are onboarded safely with zero cross-tenant visibility.

-- POSTGRESQL'S CATALOG ARCHITECTURE - self hosting metadata system where the database stores it's own schema, configuration and internal bookkeeping inside regular tables managed by the engine itself
-- Examples
-- 1. pg_catalog - manages all system tables. pg_catalog schema is implicitly present in the search path of every database
-- 2. pg_authid - manages database roles(users)
-- 3. pg_namespace - manages schema namespaces

-- BULDING A MULTI-TENANT ENVIRONMENT INSIDE A SINGLE POSTGRESQL DATABASE
-- 1. Cluster-Scoped Roles vs. Database-Scoped Schemas
-- Cluster-Scoped Roles - Database users(roles) are stored in the shared system catalog(pg_authid) and a role created in one database exists across the entire server cluster globally. 
-- Database-Scoped Schemas - Schemas are logical namespaces stored inside a specific database's pg_namespace catalog

-- 2. The search_path Resolution Chain
-- Whenever a query references an unqualified table name(e.g SELECT * FROM SHIPMENTS), PostgreSQL walks through the session's search_path list from left to right and binds to the first matching object it finds. 
-- By default, PostgreSQL sets search_path to public

-- 3. The public Schema Hijack Vulnerability
-- In older PostgreSQL versions(prior to pg15), the pseudo-role PUBLIC(every role on the cluster) was granted CREATE and USAGE privileges on the public schema by default. 
-- If Tenant A creates a table or a function in public, and Tenant B runs an unqualified query where Tenant B's own schema lacks that object, PostgreSQL falls back to public and executes Tenant A's object leading to silent data leaks. 

-- Therefore, to eliminate cross tenant visibility and data leaks, every tenant role is locked strictly inside its own namespace and severing all default shared pathways.


-- 1. Create the isolated tenant login role with zero cluster-level creation powers
-- tenant_acme_user & tenant_globex_user - placeholder identifiers used in software development and database schemas to represent a ficitional client/customer in a multi-tenant system


REVOKE CONNECT ON DATABASE logistics_production FROM PUBLIC;
-- Prevent unprivileged roles from PUBLIC from CONNECTING to the database logistics_production

REVOKE ALL ON SCHEMA public FROM PUBLIC


-- 3. Install shared extensions into a dedicated utility schema
CREATE SCHEMA IF NOT EXISTS extensions;
CREATE EXTENSION IF NOT EXISTS pgcrypto SCHEMA extensions;

-- Allow tenants to invoke extension functions (e.g., gen_random_uuid) without modifying them
GRANT USAGE ON SCHEMA extensions TO PUBLIC;

BEGIN;


DROP DATABASE IF EXISTS logistics_production;
CREATE DATABASE logistics_production;

REVOKE ALL ON DATABASE logistics_production FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM PUBLIC;

CREATE ROLE tenant_acme_user WITH
    LOGIN PASSWORD 'tenantAcmeUserDatabase'
    NOSUPERUSER
    NOCREATEDB
    CREATEROLE
    NOREPLICATION
    CONNECTION LIMIT 50;

GRANT CONNECT ON DATABASE logistics_production TO tenant_acme_user;
-- prevent unprivileged users from connecting to the database logistics_production
CREATE SCHEMA IF NOT EXISTS extensions;
CREATE EXTENSION IF NOT EXISTS pgcrypto SCHEMA extensions;

GRANT USAGE ON SCHEMA extensions TO PUBLIC;

CREATE SCHEMA tenant_acme AUTHORIZATION tenant_acme_user;

CREATE TABLE tenant_acme.shipments(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tracking_code TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL DEFAULT 'pending'
        CHECK(status IN ('pending', 'in_transit', 'delivered')),
    created_at TIMESTAMPZ NOT NULL DEFAULT NOW()
)

ALTER TABLE tenant_acme.shipments OWNER to tenant_acme_user;

-- -- 1. Prevent unprivileged roles from connecting to other databases by default
-- REVOKE CONNECT ON DATABASE logistics_production FROM PUBLIC;

-- -- 2. Seal off the shared 'public' schema completely
-- REVOKE ALL ON SCHEMA public FROM PUBLIC;

-- -- 3. Install shared extensions into a dedicated utility schema
-- CREATE SCHEMA IF NOT EXISTS extensions;
-- CREATE EXTENSION IF NOT EXISTS pgcrypto SCHEMA extensions;

-- -- Allow tenants to invoke extension functions (e.g., gen_random_uuid) without modifying them
-- GRANT USAGE ON SCHEMA extensions TO PUBLIC;

-- sql
-- BEGIN;

-- -- 1. Create the isolated tenant login role with zero cluster-level creation powers
-- CREATE ROLE tenant_acme_user WITH
--     LOGIN
--     PASSWORD 'Strong_Generated_Secret_Here'
--     NOSUPERUSER
--     NOCREATEDB
--     CREATEROLE
--     NOREPLICATION
--     CONNECTION LIMIT 50;

-- -- 2. Grant explicit connection rights only to the production database
-- GRANT CONNECT ON DATABASE logistics_production TO tenant_acme_user;

-- -- 3. Create the tenant's private schema and assign direct ownership
-- CREATE SCHEMA tenant_acme AUTHORIZATION tenant_acme_user;

-- -- 4. Lock the role's search_path at the catalog level
-- -- Notice 'public' is completely omitted; 'extensions' sits at the end for UUID functions
-- ALTER ROLE tenant_acme_user IN DATABASE logistics_production
--     SET search_path TO tenant_acme, extensions;

-- -- 5. Provision core tenant tables inside their isolated namespace
-- CREATE TABLE tenant_acme.shipments (
--     id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
--     tracking_code TEXT NOT NULL UNIQUE,
--     status TEXT NOT NULL DEFAULT 'pending'
--         CHECK (status IN ('pending', 'in_transit', 'delivered')),
--     created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
-- );

-- -- Ensure ownership of all provisioned objects belongs to the tenant role
-- ALTER TABLE tenant_acme.shipments OWNER TO tenant_acme_user;

-- COMMIT;

-- EXTENSIONS SCHEMA
It keeps extension objects out of public.

Cleaner public: extensions like pgcrypto add dozens of functions. Putting them in extensions means public only holds your own tables and functions.
Fewer name collisions: your own function names can't clash with the extension's.
Security: public is writable by many roles, and anything there can shadow or be confused with trusted functions. A dedicated schema with tighter privileges is safer.
Easier permissions and dumps: you can grant, revoke, or exclude the extensions schema as one unit.


Same extension, two setups.

Scenario 1: pgcrypto in public

sql
CREATE EXTENSION pgcrypto;  -- defaults to public

CREATE TABLE users (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  email text,
  password_hash text
);

-- Works unqualified
INSERT INTO users (email, password_hash)
VALUES ('a@x.com', crypt('secret', gen_salt('bf')));

\df public.*   -- your functions + ~40 pgcrypto functions mixed together

Problem: if you later write your own public.digest(...), it collides with pgcrypto's digest. Any role with CREATE on public can also add a function that shadows a trusted one.

Scenario 2: pgcrypto in extensions

sql
CREATE SCHEMA IF NOT EXISTS extensions;
CREATE EXTENSION pgcrypto SCHEMA extensions;

-- Unqualified now fails
INSERT INTO users (email, password_hash)
VALUES ('a@x.com', crypt('secret', gen_salt('bf')));
-- ERROR: function crypt(unknown, text) does not exist

-- Qualify it...
INSERT INTO users (email, password_hash)
VALUES ('a@x.com', extensions.crypt('secret', extensions.gen_salt('bf')));

-- ...or add it to the search_path
SET search_path TO public, extensions;
-- now unqualified calls work again

\df public.*      -- only your functions
\df extensions.*  -- only pgcrypto's

pgcrypto is a PostgreSQL extension that enables you to encrypt, decrypt, hash, and create digital signatures within your database. At Timescale, we know how precious your data is and fully recognize the significance of safeguarding sensitive information.
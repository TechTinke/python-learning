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
-- Cluster-Scoped Roles - Database users(roles) are stored in the shared system catalog(pg_authid) and a role created in one database exists across the entire server cluster. 
-- Database-Scoped Schemas - Schemas are logical namespaces stored inside a specif database's pg_namespace catalog

-- 2. The search_path Resolution Chain
-- Whenever a query references an unqualified table name(e.g SELECT * FROM SHIPMENTS), PostgreSQL walks through the session's search_path list from left tot right and binds to the first matching object it finds. 
-- By ddefault, PostgreSQL sets search_path to public

-- 3. The public Schema Hijack Vulnerability
-- In older PostgreSQL versions(prior to pg15), the pseudo-role PUBLIC(every role on the cluster) was granted CREATE and USAGE privileges on the public schema by default. 
-- If Tenant A creates a table or a function in public, and Tenant B runs an unqualified query where Tenant B's own schema lacks that object, PostgreSQL falls back to public and executes Tenant A's object leading to silent data leaks. 

-- Therefore, to eliminate cross tenant visibility and data leaks, every tenant role is locked strictly inside its own namespace and severing all default shared pathways.




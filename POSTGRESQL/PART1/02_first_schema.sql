-- CREATE SCHEMA enters a new schema into the current database
-- The name of the schema must be distinct from the name of any existing schema in the existing database

-- -> Schema - A schema is essentially a namespace
-- A schema contains named objects(tables, data types, functions and operators)whose names can duplicate those of other objects existing in other schemas
-- These objects can be accessed either by "qualifying" their names with the schema name as a prefix or by setting a search path that includes the desired schema(s)

-- Optionally, CREATE SCHEMA can include sub commands to create objects within the new schema.
-- These subcommands are treated essentially the same as seperate commands issued after creating the schema,except that if the AUTHORIZATION clause isused, all
-- the created objects will be owned by that user

-- PARAMETERS
-- -> 1. schema_name - name of the schema to be created.
-- If omitted,the user_name is used as the schema_name.
-- The name cannot begin with pg_ as those names are reserved for system schemas

-- -> 2. user_name - role name of the user who will own the new schema
-- If omitted, it defaults to the user executing the command of creating the schema. 
-- To create a schema owned by another role, you must be able to set SET ROLE to that role
 
-- -> 3. schema_element - an sql statement defining the object to be created within the schema
-- Currently,only CREATE TABLE,CREATE VIEW,CREATE INDEX,CREATE SEQUENCE,CREATE TRIGGER and GRANT are accepted asclauses within CREATE SCHEMA
-- Other kinds of objects might be created in separate commands after the schema is created

-- -> 4. IF NOT EXISTS - do nothing(except issue a notice)if a schema with the same name already exists 

-- To create a schema, the invoking user must have the CREATE privilege for the current database


CREATE SCHEMA IF NOT EXISTS basics;

CREATE EXTENSION IF NOT EXISTS pgcrypto;


SELECT schema_name
FROM information_schema.schemata
ORDER BY schema_name;
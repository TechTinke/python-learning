-- High-Frequency IoT Network

-- A smart-city infrastructure network tracks millions of environmental sensors(air-quality, temperature, acoustic noise) across five distinct geographic zones.
-- Data from each zone is managed independently by different data engineering teams who should not accidentally access or overwite each other's structures, yet global city analysts mmust run aggregate queries across all zones simultaneously.
-- Design the logical namespace strategy to solve this.

-- DATABASE ROLES AND PRIVILEGES
-- PostgreSQL manages database access permissions using the concept of roles.
-- A role can be thought of as a database user, a group of database users depending on how the role is set up. Any role can act as a user, a group or both
-- Roles can own database objects(tables, indexes, sequences or views) and can assign privileges on those objects to other roles to control who has access to which objects

-- Database roles are conceptually different from operating system users but in practise, it might be convinient to maintain a correspondence

-- To create a role use the CREATE ROLE commmand
-- CREATE ROLE analytics_team_role 
 
-- In practise, you usually want to add additional options, such as LOGIN, to the CREATE ROLE command.

-- To remove an existing role, you use the analogous DROP ROLE command  
-- DROP ROLE analytics_team_role

-- the programs createuser and dropuser are provided as wrappers around the SQL commands, CREATE ROLE and DROP ROLE respectively and can be called from shell command line
-- \du -> listing existing roles

-- In order to bootstrap the database system, a freshly initiliazed system always has one predefined role. The role is always a "superuser", and by default(unless altered when running initdb)the superuser will have the same name as the operating system user that initialized the database cluster.
-- Customarily, this role will be named postgres
-- In order to create more roles, you first have to connect as this initial role

-- Every connection made to the database server is made in the name of a particular role , and this role determines the initial access privileges for commands issued on that connection. 
--  The role name to use for a particular database connection is indicated by the client that is initiating the connection request in an application-specific fashion

-- ROLE ATTRIBUTES
-- A database role may have a number of attributes that define its privileges and interact with the client authentication system

-- 1. login privilege
-- Only roles that have the LOGIN attribute can be used as the initial role for a database connection.
-- A role with the LOGIN attribute can be considered the same thing as a "database user". 
-- To create a role with login privilege, use either

-- CREATE ROLE database_analytics_team LOGIN; OR
-- CREATE USER database_analytics_team -> CREATE USER assumes the LOGIN attribute by default, while CREATE ROLE does not 

-- 2. superuser status
-- A database superuser bypasses all permission checks
-- This is a dangerous privilege and should not be used carelessly; it is best to do most of your work as a role that is not a superuser. 
-- To create a new database superuser, use

-- CREATE ROLE database_analytics_team SUPERUSER

-- 3. database creation
-- A role must be explicitly given permission to create databases(except for superusers, since those bypass all permission checks)
-- To create such a role use,

-- CREATE ROLE database_analytics_team CREATEDB

-- 4. role creation
-- A role must be explicitly given permission to create more roles(except for superusers, since those bypass all permission checks)
-- To create such a role, use

-- CREATE ROLE database_anyltics_team CREATEROLE

-- A role with CREATEROLE privilege can alter and drop other roles, too, as well as grant or revoke membership in them.
-- However, to create, alter, drop or change membership of a superuser role, superuser status is required; CREATEROLE is not sufficient for that

-- 5. password
-- A password is only significant if the client authentication method requires the user to supply a password when connecting to the database.
-- The i) password, ii) md5 iii) crypt authentication methods make use use of passwords
-- Database passwords are seperate from operating system passwords
-- Specify a password upon role creation with 
-- CREATE ROLE database_anaytics_team PASSWORD 'string';

-- A role's attributes can be modified after creation with ALTER ROLE

-- PRIVILEGES
-- When an object is created, it is assigned an owner. 
-- The owner is normally the role that executed the creation statement. 
-- For most objects, the initial state is that only the owner(or a superuser) can do anything with the object. 
-- To allow other roles to use it, privileges must be granted. 
-- There are several kinds of privileges;
-- SELECT
-- INSERT
-- UPDATE
-- DELETE
-- RULE
-- REFERENCES
-- TRIGGER
-- CREATE
-- TEMPORARY
-- EXECUTE
-- USAGE

-- To assign privileges, the GRANT command is used. 

-- GRANT SELECT ON operational_reporting.environmental_readings TO analytics_team_role;
-- The secial privileges of an object's owner (i.e the right to modify or destroy the object) are always implicit in being the owner, and cannot be granted or revoked. 
-- However, the ower can choose to revoke his own ordinary privileges e.g make a table read-olny for himself as well as others

-- An object can be assigned to a new onwer with an ALTER command of the appropriate kid for the object. 
-- Superusers can always fo this; ordinary roles can only do it if they are both the current owner of the object(or a member of the owning role) and a member of the new owning role. 

-- ROLE MEMBERSHIP
-- It is frequently convinient to group users together to ease management of privileges; that way, privileges can be granted to, revoked from, a grou as a whole. 
-- This is done by creating a role that representa the group, and then granting membership in the group role to individual user roles
-- Once the group role exists, you can add or remove members using GRANT and REVOKE commands

-- GRANT group_role TO role1
-- REVOKE group_role FROM role1

-- You can grant membership to other group roles, too(since there isn't really any distinction between group roles and non-group roles). 
-- The database will not let you set up circular membership roles. 
-- Also, it is not permitted to grant membership in a role to PUBLIC

-- The members of a role can use the privileges of the group role in two ways. 
-- FIRST, every member of a group can explicitly do SET ROLE to "temporarily" become the group role. 
-- In this state, the database session has access to the privileges  of the group role rather than the original login role, and any database objects created are considered owned by the group role and not the login role. 
-- Second, member roles that have the INHERIT attribute automatically have use of privileges of roles they are members of. 

-- CREATE ROLE joe LOGIN INHERIT;
-- CREATE ROLE admin NONINHERIT;    
-- CREATE ROLE wheel NONINHERIT;
-- GRANT admin TO joe;
-- GRANT wheel TO admin;

-- Immediately after connecting as role joe, a database session will have use of privileges granted directly to joe plus any privilges granted to admin, because joe "inherits" admin's privileges. 
-- However, privileges granted to wheel are not available, because even though joe is indirectly a member of wheel, the membership is via admin which has NONINHERIT attribute. 

-- After SET ROLE admin; the database session would have use of only those privileges granted to admin, and not those granted to joe. 

-- After SET ROLE wheel; the database session would have use of only those privileges granted to wheel, and not those granted to either joe or admin. 

-- The original privilege state can be restored with any of
-- SET ROLE joe;
-- SET ROLE NONE;
-- RESET ROLE;

-- FUNCTIONS AND TRIGGERS
-- Functions and triggers allow users to insert code into the backend server that other users may execute uintentionally. 
-- Hence, both mechanisms permit users to "Trojan horse" others with relative ease. 
-- The only real protection is tight control over who can define functions

-- Functions run inside the backend server process with the operating system permissions of the database server daemon. 
-- If the programming language used for the function allows unchecked memory accesses, it is possible to change the server's internal data structures. 
-- Hence, among many other things, such functions can circumvent any system access controls. 
-- Function languages that allow such access are considered "untrusted", and PostgreSQL allows only superusers to create functions written in those languages. 

-- database engine roles creation
CREATE ROLE analytics_team WITH NOLOGIN; 
CREATE ROLE zone_north_team WITH NOLOGIN;
CREATE ROLE zone_south_team WITH NOLOGIN;

-- isolated namespace boundaries
CREATE SCHEMA zone_north AUTHORIZATION zone_north_team;
CREATE SCHEMA zone_south AUTHORIZATION zone_south_team;
CREATE SCHEMA operational_reporting AUTHORIZATION analytics_team;


CREATE TABLE operational_reporting.environmental_readings (
    reading_id BIGINT NOT NULL,
    zone_id VARCHAR(16) NOT NULL,
    sensor_id UUID NOT NULL,
    captured_at TIMESTAMPTZ NOT NULL,
    -- TIMESTAMPZ(Timestamp with time zone) - converts your timestamps to UTC for internal storage and automatically translates them back to your local session time zone when queried
    -- TIMESTAMP(without time zone) - completely ignores time offsets which frequently causes timezone mismatch bugs down the road
    metric_type VARCHAR(32) NOT NULL,
    metric_value DOUBLE PRECISION NOT NULL
) PARTITION BY LIST (zone_id);

CREATE TABLE zone_north.readings_north 
    PARTITION OF operational_reporting.environmental_readings
    FOR VALUES IN ('ZONE_NORTH');

CREATE TABLE zone_south.readings_south 
    PARTITION OF operational_reporting.environmental_readings
    FOR VALUES IN ('ZONE_SOUTH');

ALTER TABLE zone_north.readings_north OWNER TO zone_north_team;
ALTER TABLE zone_south.readings_south OWNER TO zone_south_team;

GRANT USAGE ON SCHEMA operational_reporting TO analytics_team_role;
GRANT SELECT ON operational_reporting.environmental_readings TO analytics_team_role;

GRANT USAGE ON SCHEMA zone_north, zone_south TO analytics_team_role;
GRANT SELECT ON zone_north.readings_north, zone_south.readings_south TO analytics_team_role;
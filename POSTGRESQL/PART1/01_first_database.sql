-- Dropping a database completely removes the database
-- It's risky to do this during production as you are dealing with real data
DROP DATABASE IF EXISTS postgresql_part1;

-- Creating a new database inside postgresql server
CREATE DATABASE postgresql_part1;

-- psql -U postgres -d postgres -f PART 1/01_first_database.sql
-- -> Use psql - PostgreSQL
-- -> Login as postgres user
-- -> Connect to postgres database
-- -> Run the SQL file- PART 1/01_first_database.sql

-- sudo -u postgres psql -d postgres -f PART1/01_first_database.sql

-- PEER AUTHENTICATION - security method that verifies the identity of a connecting user by checking system-level attributes rather than requiring a password or token
-- On many Linux systems, the local PostgreSQL configuration uses peer authentication and that means Ubuntu/Linux checks whether the Linux/Ubuntu username is postgres 
-- and if not it returns an error(psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  Peer authentication failed for user "postgres")
-- In that case, the command -- sudo -u postgres psql -d postgresql_part1 -- is used
-- It tells Linux to run psql as Linux postgres user

-- ALTERNATIVE for: psql -U postgres -d postgres -f PART 1/01_first_database.sql -> Results in a peer authentication error if the Linux/Ubuntu username is not postgres
-- sudo -u postgres psql -d postgres -f PART1/01_first_database.sql 
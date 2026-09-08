-- Dropping a database completely removes the database
-- It's risky to do this during production as you are dealing with real data
DROP DATABASE IF EXISTS postgresql_part1

-- Creating a new database inside postgresql server
CREATE DATABASE postgresql_part1

-- psql -U postgres -d postgres -f PART 1/01_first_database.sql
-- -> Use psql - PostgreSQL
-- -> Login as postgres user
-- -> Connect to postgres database
-- -> Run the SQL - PART 1/01_first_database.sql
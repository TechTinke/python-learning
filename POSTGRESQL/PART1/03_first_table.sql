-- Tables are used to store data and they are created inside a schema

DROP TABLE IF EXISTS basics.students;
-- It is rsiky to use this in a real world project because you are working with actual data

CREATE TABLE basics.students (
    id SERIAL PRIMARY KEY,
    -- SERIAL -> create an auto incrementing integer 
    -- PRIMARY KEY -> column that uniquely identifies each row
    name TEXT NOT NULL,
    -- TEXT - string data
    -- NOT NULL- this column is required
    email TEXT NOT NULL UNIQUE,
    -- UNIQUE - each student has their own unique email
    age INTEGER CHECK(age >= 18), 

    -- TIMESTAMP -> Stores date and time format
    created_at TIMESTAMP DEFAULT NOW()
);

-- NB:
-- Single quotes ' ' - string/text
-- Double quotes " " - column/table identifiers

INSERT INTO basics.students(name, email, age)
VALUES
  ('Oscar', 'oscar@gmail.com', 18),
  ('Erick', 'erick@gmail.com', 20),
  ('Myke', 'myke@gmail.com', 22);

SELECT * FROM basics.students;

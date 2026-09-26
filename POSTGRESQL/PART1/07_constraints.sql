-- SQL allows you to define constraints on columns and tables
-- Constraints give you as much control over the data in your tables as you wish
DROP TABLE basics.accounts;

CREATE TABLE basics.accounts(
    id SERIAL PRIMARY KEY,

    full_name TEXT NOT NULL,
    -- 2. NOT NULLCONSTRAINT
    -- -> It simply specifies that a column must not assume the null value

    email TEXT NOT NULL UNIQUE,
    -- 3. UNIQUE CONSTRAINT
    -- -> Ensure the data contained in a column, or a group of columns, is unique among all the rows in the table
    -- As a table constraint, a UNIQUE constraint is defined as:
    -- UNIQUE(email)

    -- To define a unique constraint for a group of columns, write it as a table constraint with column names separated by commas
    -- UNIQUE(full_name, email, age)
    is_active BOOLEAN DEFAULT true,

    age INTEGER CHECK (age >= 18),
    -- 1. CHECK CONSTRAINT
    -- ->It allows you to specify that the value in a certain column must satisy a Boolean(truth-value) expression e.g require positive product prices
    -- product_price NUMERIC CHECK(price > 0)
    -- You can give the constraint a different name. This clarifies error messages and allows yu to refer to the constraint when you need to change it otherwise the system chooses a name for you
    
    -- age INTERGER CONSTRAINT adult_age CHECK(age > 18)
    -- ERROR:  new row for relation "accounts" violates check constraint "adult_age"


    created_at TIMESTAMP DEFAULT NOW()
);

-- INSERT INTO basics.accounts(full_name, email, age)
-- VALUES('elon musk', 'elonmusk@gmail.com', 56);

-- SELCT * FROM basics.accounts;
-- INSERT INTO basics.accounts(email,age)
-- VALUES
-- ('noname@gmail.com', 46)
-- ERROR: null value in column "full_name" of relation "accounts" violates not-null constraint

-- INSERT INTO basics.accounts(full_name, email, age)
-- VALUES
-- ('abelpatrick', 'abelpatrick@gmail.com', 63),
-- ('briankiteme', 'abelpatrick@gmail.com', 56);
--  ERROR:  duplicate key value violates unique constraint "accounts_email_key"
-- DETAIL:  Key (email)=(abelpatrick@gmail.com) already exists.

INSERT INTO basics.accounts(full_name, email, age)
VALUES
('abelpatrick', 'abelpatrick@gmail.com', 17);
-- ERROR:  new row for relation "accounts" violates check constraint "accounts_age_check"
-- DETAIL:  Failing row contains (1, abelpatrick, awwabelpatrick@gmail.com, t, 17, 2026-09-23 23:22:23.752328).
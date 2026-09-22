-- SQL allows you to define constraints on columns and tables
-- Constraints give you as much control over the data in your tables as you wish
DROP TABLE basics.accounts;

CREATE TABLE basics.accounts(
    id SERIAL PRIMARY KEY,

    full_name TEXT NOT NULL,

    email TEXT NOT NULL,

    is_active BOOLEAN DEFAULT true,

    age INTEGER CHECK (age >= 18),

    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO basics.accounts(full_name, email, age)
VALUES('elon musk', 'elonmusk@gmail.com', 56);

-- SELCT * FROM basics.accounts;

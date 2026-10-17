-- A primary key uniquely identifies each row in a table
-- A primary key indicates that a column or a group of columns can be used as unique identifiers for rows in that table
-- Primary keys can span more than one column
-- Adding a primary key to a column automatically creates a unique B-tree index on the column or group of columns listed in the primary key and will force the the column(s) to be marked NOT NULL
-- Without a primary key, it becomes harder to update, delete or do any kind of reference or connecting a specific row to rows in other tables

-- Primary keys are useful for both documentation and client applications
-- For example a GUI application that allows modifying row values probably needs to know the primary key of a table to be able to identify rows uniquely.
-- Primary keys also define the default target column(s) for foreign keys referencing its table

DROP TABLE IF EXISTS basics.sales;

CREATE TABLE basics.sales(
    id SERIAL PRIMARY KEY,

    title TEXT NOT NULL,

    price NUMERIC(10, 2) NOT NULL DEFAULT 0,

    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO basics.sales(title, price)
VALUES
('sale1', 200),
('sale2', 500);

-- SELECT * FROM basics.sales;
SELECT * FROM basics.sales WHERE id = 2;
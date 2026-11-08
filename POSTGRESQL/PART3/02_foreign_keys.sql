-- Foreign key - column that points to the primary key of another table
-- A foreign key constrait specifies that the values in a column or a group of columns must match the values appearing in some row of another table.
-- This maintains the referential integrity between two related tables
-- A foreign key constraint is defined in the child table referencing the parent table. 

-- product table - stores the products(referenced table)
CREATE TABLE products(
    product_no INTEGER PRIMARY KEY, 
    name VARCHAR(16),
    price NUMERIC(6,2)
)

-- orders table(referencing table)- storing orders of the products in the products table
-- The orders table should only contain orders of prdoucts that actually exist. 
-- To enforce that, a foreign key constraint is defined in the orders table that references the products table

CREATE TABLE orders(
    order_id integer PRIMARY KEY,
    product_no INTEGER REFERENCES products(product_no)
    -- product_no INTEGER REFERENCES products
    -- In the absence of a column list(products(product_no)), the primary key of the referenced table is used as the referenced column(s)

)

-- Now that way, it is impossible to create orders with non-NULL product_no entries that do not appear in the products table
-- In this situation, the products table is the referenced table while the orders table is the referencing table.
-- Similarly, there are referenced and referencing columns

-- A foreign key can also constrain and reference a group of columns. 
-- The number and type of the constrained columns need to match the number and type of the referenced columns. 

-- A table can have more than one foreign key constraint. 
-- This is what is used to implement many-to-many relationships between tables (One order can cotain possibly many products)

CREATE TABLE products(
    product_no INTEGER PRIMARY KEY,
    name TEXT,
    price NUMBERIC(4,2)
);

CREATE TABLE orders(
    order_id INTEGER PRIMARY KEY,
    shipping_address TEXT,
),

CREATE TABLE order_items(
    product_no INTEGER REFERENCES products,
    order_id INTEGER REFERENCES orders,
    quantity INTEGER,
    PRIMARY KEY(product_no, order_id)
);

-- In our example, foreign keys disallow creation of orders that do not relate to any products
-- PostgreSQL disallows the deletion of a product that is already referenced by an order( via order_items)

CREATE TABLE products(
    product_no INTEGER PRIMARY KEY,
    name TEXT,
    price NUMBERIC(4,2)
);

CREATE TABLE orders(
    order_id INTEGER PRIMARY KEY,
    shipping_address TEXT,
),

CREATE TABLE order_items(
    product_no INTEGER REFERENCES products,
    order_id INTEGER REFERENCES orders,
    quantity INTEGER,
    PRIMARY KEY(product_no, order_id)
);

-- 1. NO ACTION - default ON DELETE ACTION that does not need to be specified
-- ON DELETE NO ACTIO  allows deletion of the referenced table to proceed but this results in an error as the foreign key constraint is still required to be satisfied
-- The foreign constraint check can also be deferred to later in the transaction

-- 2.  RESTRICT - a stricter setting than NO ACTION. 
-- ON DELETE RESTRICT prevents the deletion of a referenced row. 
-- ON DELETE RESTRICT does not allow rhe check to be deferred until later in the transaction. 

-- 3. CASCADE
-- ON DELETE CASCADE - specifies that when a referenced row is deleted, row(s) referencing it should be deleted as well.

-- There are two other options; SET NULL and SET DEFAULT
-- 1. SET NULL
-- These causes the referencing column(s) to be set to nulls once the referenced row is deleted. 
-- 2. SET DEFAULT
-- This causes the referencing column(s) to be set to their default values once the referenced row is deleted. 
-- However, these do not excuse you from observing any constraints. e.g If an action specifies SET DEFAULT but the default value would not satisfy the foreign key constraint, the operation will fail/result into an error

-- The appropriate choice of ON DELETE action depends on the kinds of objects the related tables represent. 
-- When the referencing table represets something that is a component of what is represented by the referenced table and cannot exist independently, then ON DELETE CASCADE would be appropriate. 
-- If two tables represent independent objects, then ON DELETE CASCADE or ON DELETE NO ACTION would be appropriate. 
-- An application that actually wants to delete both objects would have  to be explicit about this and run two commands. 
-- In our example, order items are part of an order and it is convinient that they are deleted automatically if an order is deleted. 
-- But products and orders are different things, so making the deletion of a roduct automatically causes the deletion of some order items and that would be considered problematic. 
-- The actions SET NULL or SET DEFAULT can be approriate if a foreign key relationship  represents optional information. 
-- For example, if the products table contained a reference to a product manager, and the product manager entry gets deleted, then setting the product's product manager to null or a default value might be useful/appropriate. 

-- The actions SET NULL or SET DEFAULT ca take a column list to specify which columns to set. 
-- Normally, all columns of the foreign-key constraint are set butting setting only a subset of the columns is useful in some cases. 

-- EXAMPLE
CREATE TABLE tenants (
    tenant_id integer PRIMARY KEY
);

CREATE TABLE users (
    tenant_id integer REFERENCES tenants ON DELETE CASCADE,
    user_id integer NOT NULL,
    PRIMARY KEY (tenant_id, user_id)
);

CREATE TABLE posts (
    tenant_id integer REFERENCES tenants ON DELETE CASCADE,
    post_id integer NOT NULL,
    author_id integer,
    PRIMARY KEY (tenant_id, post_id),
    FOREIGN KEY (tenant_id, author_id) REFERENCES users ON DELETE SET NULL (author_id)
);

-- Without the spicification of the column, the foreign key would sert the column tenant_id to NULL, but that column is required as part of the primary key. 

-- Analogous to ON DELETE there is also ON UPDATE which is invoked when a referenced column is changed(updated). 
-- The possible actions are the same, excet that column lists cannot be specified for SET NULL and SET DEFAULT. 
-- 1. ON UPDATE CASCADE
-- The updated values of the referenced column(s) should be copied into the referencing row(s). 

-- 2. ON UPDATE NO ACTION
-- Allows the update to proceed and the foreign key constraint will be checked against the state after the update

-- 3. ON UPDATE RESTRICT
-- It will prevent the update to run even if the state after the update would still satisfy the constraint preventing updating a referenced row to a value that is distinct but compares as equal(for example, a character string with a different case variant, if a character string type with a case-insensitive collation is used).

-- A foreign key must reference columns that either are a primary key or form a unique constraint, or are columns from a non-partial unique index.
-- This means that the referenced columns always have an index to allow efficient lookups on whether a referencing row has a match.
-- Since a DELETE of a row from the referenced table or an UPDATE of a referenced column will require a scan of the referencing table for rows matching the old value, it is often a good idea to index the referencing columns too.
-- Because this is not always needed, and there are many choices available on how to index, the declaration of a foreign key constraint does not automatically create an index on the referencing columns.



-- users.id  - parent key
-- posts.user_id - foreign key
-- Every post created must belong to an existing user

SELECT id, name
FROM basics.users;

SELECT user_id, title
FROM basics.posts;
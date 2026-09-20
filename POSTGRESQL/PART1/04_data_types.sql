DROP TABLE IF EXISTS basics.products_basic;

CREATE TABLE basics.products_basic(
    id SERIAL PRIMARY KEY,

    name VARCHAR(100) NOT NULL,
    -- VARCHAR(100) - string that has a maximum length of 100 characters

    description TEXT,

    stock INTEGER DEFAULT 0,
    -- INTEGER - stores whole numbers

    total_views BIGINT DEFAULT 0,
    -- BIGINT - store a larger whole number than INTEGER

    price NUMERIC(10,2),
    -- 10 - total digits
    -- 2 - digits after the decimal
    -- NUMERIC - when storing an exact number of decimal places

    is_active BOOLEAN DEFAULT true
);

INSERT INTO basics.products_basic(name, description, stock, total_views, price, is_active)
VALUES
   ('product_1',
   'product_1 description',
   100,
   1200,
   2455.65,
   true),
   ('product_2',
   'product_2 description',
   34,
   4567,
   256.00,
   false);

SELECT * FROM basics.products_basic;

SELECT id, name, price, is_active
FROM basics.products_basic
WHERE is_active;

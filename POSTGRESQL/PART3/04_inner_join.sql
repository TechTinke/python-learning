-- JOIN Clause - used to combine rows from two or more tables, based on a related column between them

-- There are four types of JOINS;

-- INNER JOIN - returns only the matching rows from both tables/Returns records that have matching values in both tables-- LEFT JOIN - 
-- LEFT JOIN - Returns all records from the left table, and the matched records from the right table
-- RIGHT JOIN - Returns all records from the right table , and the matched records from the left table
-- FULL JOIN - Returns all recors when there is a match in either left or right table
-- CROSS JOIN - Returns the Cartesian product of two or more table(combines every row from the first table with every row from the second table)
-- EXAMPLE 1
-- SELECT
-- basics.users.name AS author_name,
-- basics.posts.title AS post_title,
-- basics.posts.status,
-- basics.posts.views
-- FROM basics.posts
-- INNER JOIN basics.users
-- ON basics.posts.user_id = basics.users.id
-- WHERE basics.posts.status = 'published'
-- ORDER BY basics.posts.views DESC;

-- EXAMPLE 2
DROP TABLE IF EXISTS basics.products;
DROP TABLE IF EXISTS basics.categories;

CREATE TABLE basics.categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(30),
    description VARCHAR(100)
);

CREATE TABLE basics.products(
    product_id SERIAL  PRIMARY KEY,
    product_name VARCHAR(30),
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES basics.categories(category_id)
);

INSERT INTO basics.categories(category_name, description)
VALUES
('Beverages', 'Soft drinks, coffees, teas, beers, and ales'),
('Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings'),
('Confections', 'Desserts, candies, and sweet breads'),
('Dairy Products', 'Cheeses'),
('Grains/Cereals', 'Breads, crackers, pasta, and cereal'),
('Meat/Poultry', 'Prepared meats'),
('Produce', 'Dried fruit and bean curd'),
('Seafood', 'Seaweed and fish');
INSERT INTO basics.products(product_name, category_id)
VALUES
('Geitost', 4),
('Sasquash Ale', 1),
('Steeleye Stout', 1),
('Inlagd Sill',2 );

SELECT * FROM basics.categories;
SELECT * FROM basics.products;
SELECT product_id, product_name, category_name
FROM basics.products
INNER JOIN basics.categories
ON basics.products.category_id = basics.categories.category_id
ORDER BY category_name;

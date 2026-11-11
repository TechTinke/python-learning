-- EXAMPLE 1
CREATE EXTENSION IF NOT EXISTS pgcrypto;

DROP TABLE IF EXISTS basics.post_tags;
DROP TABLE IF EXISTS basics.comments;
DROP TABLE IF EXISTS basics.posts;
DROP TABLE IF EXISTS basics.tags;
DROP TABLE IF EXISTS basics.users;

CREATE TABLE basics.users(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL
);

CREATE TABLE basics.posts(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES basics.users(id),
    title TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'draft'
        CHECK (status IN ('draft', 'published')),
    views INTEGER NOT NULL DEFAULT 0 CHECK(views >= 0)
);

CREATE TABLE basics.comments(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    post_id UUID REFERENCES basics.posts(id),
    body TEXT NOT NULL
);

CREATE TABLE basics.tags(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE basics.post_tags(
    post_id UUID NOT NULL REFERENCES basics.posts(id),
    tag_id UUID NOT NULL REFERENCES basics.tags(id),
    PRIMARY KEY(post_id, tag_id)
);

INSERT INTO basics.users(name)
VALUES
('Ashley'),
('Lave');

INSERT INTO basics.posts (user_id, title, status, views)
SELECT id, 'PostgreSQL Joins Explained', 'published', 100
FROM basics.users
WHERE name = 'Ashley';

INSERT INTO basics.posts (user_id, title, status, views)
SELECT id, 'Indexes for Beginners', 'draft', 40
FROM basics.users
WHERE name = 'Ashley';

INSERT INTO basics.posts (user_id, title, status, views)
SELECT id, 'Backend APIs with PostgreSQL', 'published', 180
FROM basics.users
WHERE name = 'Lave';

INSERT INTO basics.comments (post_id, body)
SELECT id, 'Very clear explanation.'
FROM basics.posts
WHERE title = 'PostgreSQL Joins Explained';

INSERT INTO basics.comments (post_id, body)
SELECT id, 'Please add more examples.'
FROM basics.posts
WHERE title = 'Backend APIs with PostgreSQL';

INSERT INTO basics.tags(name)
VALUES
('sql'),
('backend');

INSERT INTO basics.post_tags (post_id, tag_id)
SELECT p.id, t.id
FROM basics.posts p, basics.tags t
WHERE p.title = 'PostgreSQL Joins Explained'
AND t.name = 'sql';

INSERT INTO basics.post_tags (post_id, tag_id)
SELECT p.id, t.id
FROM basics.posts p, basics.tags t
WHERE p.title = 'Indexes for Beginners'
AND t.name = 'sql';

INSERT INTO basics.post_tags (post_id, tag_id)
SELECT p.id, t.id
FROM basics.posts p, basics.tags t
WHERE p.title = 'Backend APIs with PostgreSQL'
AND t.name = 'backend';

SELECT 'Reduced database reset and sample data inserted successfully' as message;


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

SELECT product_id, product_name, category_name
FROM basics.products
INNER JOIN basics.categories
ON basics.products.category_id = basics.categories.category_id
ORDER BY category_name;
-- CREATE TABLE basics.categories(
--     category_id SERIAL INTEGER PRIMARY KEY,
--     category_name VARCHAR(30)
-- );
-- CREATE TABLE basics.products(
--     product_id SERIAL INTEGER PRIMARY KEY,
--     product_name VARCHAR(30),
--     FOREIGN KEY (category_id) REFERENCES basics.categories(category_id)
-- );
-- INSERT INTO basics.categories(category_name)
-- VALUES
-- ('Beverages'),
-- ('Condiments'),
-- ('Confections'),
-- ('Dairy Products'),
-- ('Seafood'),;
-- INSERT INTO basics.products(category_id ,product_name)
-- SELECT category_id, 'Geitost'
-- FROM basics.categories
-- WHERE category_name = 'Dairy Products';

-- INSERT INTO basics.products(category_id ,product_name)
-- SELECT category_id, 'Geitost'
-- FROM basics.categories
-- WHERE category_name = 'Beverages';

-- INSERT INTO basics.products(category_id ,product_name)
-- SELECT category_id, 'Geitost'
-- FROM basics.categories
-- WHERE category_name = 'Bevarages';

-- INSERT INTO basics.products(category_id ,product_name)
-- SELECT category_id, 'Geitost'
-- FROM basics.categories
-- WHERE category_name = 'Seafood';


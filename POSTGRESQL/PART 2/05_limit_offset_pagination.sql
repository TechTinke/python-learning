-- limit - how many rows you want to return
-- offset - how many rows we want to skip

-- SELECT name, price
-- FROM basics.products
-- ORDER BY price DESC
-- LIMIT 5;

SELECT name, price
FROM basics.products
ORDER BY price DESC
LIMIT 5 OFFSET 0;

SELECT name, price
FROM basics.products
ORDER BY price DESC
LIMIT 5 OFFSET 5;

-- OFFSET works under the principle of 
-- (page - 1) * limit
-- For example:
-- (2 - 1) * 5 = 5
-- (3 - 1) * 5 =10
-- (4 - 1) * 5 = 15

SELECT name, price
FROM basics.products
ORDER BY price DESC
LIMIT 5 OFFSET 10;
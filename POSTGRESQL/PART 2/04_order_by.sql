SELECT name, price
FROM basics.products
ORDER BY price ASC;

SELECT name, price
FROM basics.products
ORDER BY price DESC;

SELECT name, price, category
FROM basics.products
ORDER BY category ASC, price DESC;
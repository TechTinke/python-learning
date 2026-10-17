-- like - case sensitive pattern match
-- ilike - case insensitive pattern match
-- % - any no of characters
-- exactly one character

SELECT name, price, category
FROM basics.products
WHERE category LIKE 'niture%';
-- % - means anything after the pre defined characters

SELECT name, category, price
FROM basics.products
WHERE category ILIKE '%ni%';


SELECT name, category, price, description
FROM basics.products
WHERE description ILIKE '%Electronic%'
OR name ILIKE '%Electronic%';
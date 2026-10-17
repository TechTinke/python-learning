-- SELECT name, price, category, is_active
-- FROM basics.products
-- WHERE category = 'stationery';

-- UPDATE basics.products
-- SET price = ROUND(price * 1.1, 2)
-- WHERE category = 'stationery';

-- SELECT name, price, category, is_active
-- FROM basics.products
-- WHERE category = 'stationery';

UPDATE basics.products
SET is_active = FALSE
WHERE stock = 0;

SELECT name, price, category, is_active, stock
FROM basics.products
WHERE is_active = FALSE;


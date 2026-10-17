-- -> AND - every condition  must be true
-- -> OR  - at least one condition must be true
-- -> NOT - reverse/ exclude a condition

-- EXAMPLEs
-- products where it is electronics but price > 1000

-- AND 
-- SELECT name, category, price
-- FROM basics.products
-- WHERE category = 'electronics' AND price >= 1000

-- OR
-- SELECT name, category, price
-- FROM basics.products
-- WHERE category = 'electronics' OR category = 'furniture'

-- NOT
-- SELECT name, category, price
-- FROM basics.products
-- WHERE category NOT IN ('stationery', 'furniture')

-- SELECT name, category, price
-- FROM basics.products
-- WHERE category = 'furniture'

-- SELECT name, category, price
-- FROM basics.products
-- WHERE category NOT IN ('furniture', 'electronics')

SELECT name, price, category, stock
FROM basics.products
WHERE (category = 'furniture' or category = 'electronics')
AND stock >= 20


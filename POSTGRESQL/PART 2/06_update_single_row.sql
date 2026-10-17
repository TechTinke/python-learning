-- SELECT name, stock, sku
-- FROM basics.products
-- WHERE sku = 'ELEC-KEY-OO1';

UPDATE basics.products
SET price = 255.50,
    stock = 33
WHERE sku = 'ELEC-KEY-001';

SELECT name, stock, sku, price
FROM basics.products
WHERE sku = 'ELEC-KEY-001';
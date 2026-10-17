INSERT INTO basics.products(name, category, price, stock, sku, description)
VALUES('Temp product', 'electronics', 345.50, 45, 'ELEC-TEMP-013', 'Temp prdocut description');

SELECT name, category, sku
FROM basics.products
WHERE sku = 'ELEC-TEMP-013';

DELETE FROM basics.products
WHERE sku = 'ELEC-TEMP-013';

SELECT name, category, sku
FROM basics.products
WHERE sku = 'ELEC-TEMP-013';
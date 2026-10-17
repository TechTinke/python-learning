-- returning - usually returs back the rows immediately after insert

-- INSERT INTO basics.products(name, category, price, stock, sku, description)
-- VALUES('webcam', 'electronics', 455.67, 56, 'ELEC-WEB-009', 'Webcam description')
-- RETURNING id, name, category, price, stock, created_at;

-- UPDATE basics.products
-- SET stock = stock + 12
-- WHERE sku = 'ELEC-WEB-009'
-- RETURNING id, name, stock;

-- DELETE FROM basics.products
-- WHERE sku = 'ELEC-WEB-009'
-- RETURNING id, name, sku

SELECT id, name , sku
FROM basics.products
WHERE sku = 'ELEC-WEB-009';
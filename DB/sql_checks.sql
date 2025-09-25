-- SQL checks (example queries you can run in staging DB)
-- 1) Verify order created
SELECT id, user_id, total_amount, status, created_at
FROM orders
WHERE id = '<ORDER_ID>';

-- 2) Verify order items
SELECT order_id, product_id, quantity, price
FROM order_items
WHERE order_id = '<ORDER_ID>';

-- 3) Verify user address exists
SELECT id, user_id, pincode, city
FROM addresses
WHERE user_id = '<USER_ID>' AND pincode = '<PINCODE>';

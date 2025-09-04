-- Tables: Customers (id, name, city), Orders (id, customer_id, amount, date)

-- 1) Join orders with customer names
SELECT o.id, c.name, o.amount, o.date
FROM Orders o
JOIN Customers c ON o.customer_id = c.id;

-- 2) Total sales per customer
SELECT c.name, SUM(o.amount) AS total_sales
FROM Orders o
JOIN Customers c ON o.customer_id = c.id
GROUP BY c.name
ORDER BY total_sales DESC;

-- 3) Average order value
SELECT AVG(amount) AS avg_order_value
FROM Orders;

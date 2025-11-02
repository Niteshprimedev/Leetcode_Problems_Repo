# Write your MySQL query statement below
SELECT 
    p.product_name,
    o.total_units AS unit
FROM Products AS p
INNER JOIN (
    SELECT 
        product_id, 
        SUM(unit) AS total_units
    FROM Orders
    WHERE 
        EXTRACT(MONTH FROM order_date) = 2 AND 
        EXTRACT(YEAR FROM order_date) = 2020
    GROUP BY product_id 
) AS o
ON p.product_id = o.product_id
WHERE o.total_units >= 100;
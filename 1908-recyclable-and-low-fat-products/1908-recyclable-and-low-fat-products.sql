# Write your MySQL query statement below
-- SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y';

-- OR
SELECT product_id 
FROM (SELECT * FROM Products WHERE low_fats = 'Y') 
AS LowFatProducts
WHERE recyclable = 'Y';
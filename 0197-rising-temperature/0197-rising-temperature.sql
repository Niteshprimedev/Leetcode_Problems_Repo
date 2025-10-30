# Write your MySQL query statement below
SELECT w1.id AS Id
FROM Weather AS w1
JOIN Weather AS w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 -- generates 16 rows for 4 rows table => 4 * 4
WHERE w1.temperature > w2.temperature; -- filters the rows where temp1 > temp2
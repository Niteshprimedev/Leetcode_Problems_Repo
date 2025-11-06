# Write your MySQL query statement below
SELECT e.reports_to AS employee_id,
m.name, COUNT(e.reports_to) AS reports_count, ROUND(AVG(e.age)) AS average_age
FROM 
(SELECT * FROM Employees WHERE reports_to IS NOT NULL)
AS e
INNER JOIN Employees AS m
ON e.reports_to = m.employee_id
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;
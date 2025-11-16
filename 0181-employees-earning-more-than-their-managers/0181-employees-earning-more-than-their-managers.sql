# Write your MySQL query statement below
WITH Employee_With_Managers AS (
    SELECT * FROM Employee WHERE managerId IS NOT NULL
)
SELECT e.name AS Employee
FROM Employee_With_Managers AS e
INNER JOIN Employee AS m
ON e.managerId = m.id
AND e.salary > m.salary;
# Write your MySQL query statement below
WITH RankedEmployees AS (
    SELECT 
        name,
        salary,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS salaryRank,
        departmentId
    FROM Employee
), 
FilteredTopEmployees AS (
    SELECT * FROM RankedEmployees WHERE salaryRank < 4
)
SELECT 
    d.name AS Department,
    te.name AS Employee,
    te.salary AS Salary
FROM FilteredTopEmployees AS te
INNER JOIN Department AS d
ON te.departmentId = d.id;
# Write your MySQL query statement below
WITH EmployeesWithMaxSalary AS (
    SELECT MAX(salary) AS max_salary FROM Employee
)
SELECT IFNULL(MAX(salary), null) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT max_salary FROM EmployeesWithMaxSalary);
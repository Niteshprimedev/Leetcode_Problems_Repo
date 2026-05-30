# Write your MySQL query statement below
/*
WITH EmployeesWithMaxSalary AS (
    SELECT MAX(salary) AS max_salary FROM Employee
)
SELECT IFNULL(MAX(salary), null) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT max_salary FROM EmployeesWithMaxSalary);
*/

-- OR

/*
SELECT MAX(salary) OVER(ORDER BY salary DESC OFFSET 1) AS SecondHighestSalary
FROM Employee
LIMIT 1;
*/

WITH rankedSalaries AS (
    SELECT salary,
DENSE_RANK() OVER(ORDER BY salary DESC) AS salaried_rank
FROM Employee
)
SELECT IFNULL(MAX(salary), null) AS SecondHighestSalary
FROM rankedSalaries
WHERE salaried_rank = 2;
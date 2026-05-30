CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      WITH rankedSalaries AS (
        SELECT salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS salaried_rank
        FROM Employee
      )
      SELECT IFNULL(MAX(salary), NULL)
      FROM rankedSalaries
      WHERE salaried_rank = N
  );
END
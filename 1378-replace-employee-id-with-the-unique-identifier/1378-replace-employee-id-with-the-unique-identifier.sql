# Write your MySQL query statement below
SELECT eUNI.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS eUNI
ON e.id = eUNI.id;

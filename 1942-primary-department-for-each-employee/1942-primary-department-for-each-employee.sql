# Write your MySQL query statement below
SELECT 
    employee_id, 
    IFNULL(MAX(CASE WHEN primary_flag = 'Y' THEN department_id END), MIN(department_id))
    AS department_id
FROM Employee
GROUP BY employee_id;
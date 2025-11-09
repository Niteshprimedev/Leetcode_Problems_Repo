# Write your MySQL query statement below
/*SELECT m.name
FROM Employee AS e
JOIN Employee AS m
ON e.managerId = m.id
GROUP BY m.id, m.name
HAVING COUNT(e.id) >= 5;
*/

SELECT m.name
FROM Employee AS e
JOIN Employee AS m
ON e.managerId = m.id
WHERE e.managerId IS NOT NULL
GROUP BY m.id, m.name
HAVING COUNT(e.managerId) >= 5;
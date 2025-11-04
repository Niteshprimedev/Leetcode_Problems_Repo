# Write your MySQL query statement below
/*SELECT DISTINCT class
FROM Courses AS c1
WHERE 5 <= (SELECT COUNT(*) FROM Courses AS c2 WHERE c1.class = c2.class);
*/

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
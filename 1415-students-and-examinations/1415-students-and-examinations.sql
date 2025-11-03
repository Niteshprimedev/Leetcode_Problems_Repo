# Write your MySQL query statement below
/*SELECT s.student_id, s.student_name,
(SELECT sub.subject_name,
(SELECT COUNT(*) FROM Examinations AS e WHERE e.student_id = s.student_id AND e.subject_name = sub.subject_name)
AS attended_exams 
FROM Subjects AS sub)
FROM Students AS s;
*/

SELECT stud.student_id, stud.student_name,
sub.subject_name, COALESCE(COUNT(exm.subject_name), 0) AS attended_exams
FROM Students AS stud
CROSS JOIN Subjects AS sub
LEFT JOIN Examinations AS exm
ON stud.student_id = exm.student_id
AND sub.subject_name = exm.subject_name
GROUP BY stud.student_id, sub.subject_name
ORDER BY stud.student_id, sub.subject_name;
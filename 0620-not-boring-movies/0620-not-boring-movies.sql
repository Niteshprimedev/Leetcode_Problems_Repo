# Write your MySQL query statement below
/*SELECT * 
FROM Cinema
WHERE MOD(id, 2) = 1 AND description <> 'boring'
ORDER BY rating DESC;
*/

SELECT *
FROM (SELECT * FROM Cinema WHERE id % 2 = 1) AS OddCinema
WHERE description <> 'boring'
ORDER BY rating DESC;
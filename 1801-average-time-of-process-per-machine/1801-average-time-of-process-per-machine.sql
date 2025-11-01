# Write your MySQL query statement below
/*
SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM Activity AS a1
JOIN Activity AS a2
ON a1.machine_id = a2.machine_id
AND a1.process_id = a2.process_id
AND a1.activity_type = 'start'
AND a2.activity_type = 'end'
GROUP BY a1.machine_id;
*/

-- OR;
SELECT machine_id, ROUND(
    (SELECT AVG(a1.timestamp) FROM Activity AS a1 WHERE a1.activity_type = 'end' AND a1.machine_id = a.machine_id) -
    (SELECT AVG(a1.timestamp) FROM Activity AS a1 WHERE a1.activity_type = 'start' AND a1.machine_id = a.machine_id)
, 3) AS processing_time
FROM Activity AS a
GROUP BY a.machine_id;
# Write your MySQL query statement below
-- My Solution:
/*
SELECT 
    s.user_id,
    (
        IFNULL(ROUND(SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) * 1/COUNT(c.action), 2), 0)

    )
    AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c
ON s.user_id = c.user_id
GROUP BY s.user_id;
*/

/*
SELECT 
  s.user_id,
  ROUND(
    IFNULL(
      SUM(c.action = 'confirmed') / COUNT(c.action),
      0
    ), 2
  ) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c
ON s.user_id = c.user_id
GROUP BY s.user_id;
*/

WITH confirmed_users AS (
    SELECT 
        user_id,
        SUM(action = 'confirmed') AS confirmed,
        COUNT(*) AS total
    FROM Confirmations
    GROUP BY user_id
)

SELECT 
    s.user_id,
    ROUND(IFNULL(c.confirmed / c.total, 0), 2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN confirmed_users AS c
ON s.user_id = c.user_id;
# Write your MySQL query statement below
/*
WITH TotalUsers AS
(
    SELECT DISTINCT(requester_id) AS user_id FROM RequestAccepted
    UNION
    SELECT DISTINCT(accepter_id) AS user_id FROM RequestAccepted
)
SELECT 
    user_id AS id,
    total_friends AS num
FROM 
    (SELECT
        tu.user_id,
        COUNT(*) AS total_friends
    FROM TotalUsers AS tu
    INNER JOIN RequestAccepted AS ra
    ON tu.user_id = ra.requester_id OR tu.user_id = ra.accepter_id
    GROUP BY tu.user_id) AS UsersFriends
ORDER BY num DESC
LIMIT 1;
*/

-- OR UNION ALL
WITH TotalUsers AS 
(
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)
SELECT id, COUNT(*) AS num
FROM TotalUsers
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
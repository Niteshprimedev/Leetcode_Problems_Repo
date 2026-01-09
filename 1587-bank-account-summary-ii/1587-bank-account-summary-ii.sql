# Write your MySQL query statement below
SELECT
    u.name AS name,
    SUM(amount) AS balance
FROM Users AS u
INNER JOIN Transactions AS t
ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;
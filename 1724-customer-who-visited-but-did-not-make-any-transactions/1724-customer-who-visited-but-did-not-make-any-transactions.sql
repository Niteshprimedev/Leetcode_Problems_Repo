# Write your MySQL query statement below
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN (
    SELECT transaction_id, MIN(visit_id) AS visit_id, amount
    FROM Transactions
    GROUP BY visit_id
) AS t
ON v.visit_id = t.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id;
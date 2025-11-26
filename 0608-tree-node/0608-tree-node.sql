# Write your MySQL query statement below
# Observation: if a node is a parent of someone and not a root = Inner type
# if a node is not a parent of someone = leaf type
# if there is no parent of a node = root
WITH leaf_nodes AS
(
    SELECT id 
    FROM Tree 
    WHERE id NOT IN (
        SELECT p_id FROM Tree WHERE p_id IS NOT NULL
    )
)
SELECT
    t.id,
    CASE
        WHEN t.p_id IS NULL THEN 'Root'
        WHEN t.id IN (SELECT id FROM leaf_nodes) THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree t;
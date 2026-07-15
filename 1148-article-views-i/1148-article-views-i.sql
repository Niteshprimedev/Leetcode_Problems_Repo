# Write your MySQL query statement below
-- SELECT DISTINCT author_id AS id
-- FROM Views 
-- WHERE author_id = viewer_id
-- ORDER BY id ASC;

SELECT DISTINCT v1.author_id AS id
FROM Views AS v1
INNER JOIN Views as v2
ON v1.article_id = v2.article_id
AND v1.author_id = v2.viewer_id
ORDER BY id ASC;
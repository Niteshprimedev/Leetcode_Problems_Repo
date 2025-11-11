# Write your MySQL query statement below
-- Rule: len(one side) < sumOf(two sides) OR
-- Triangle Inequality Rule;
/*
SELECT 
    x, 
    y,
    z,
    (CASE
        WHEN (x + y) > z AND (y + z) > x AND (z + x) > y
        THEN 'Yes'
        ELSE 'No'
    END) AS triangle
FROM Triangle;

*/

WITH sides AS (
  SELECT x, y, z,
         (x + y) > z AS xy_gt_z,
         (y + z) > x AS yz_gt_x,
         (z + x) > y AS zx_gt_y
  FROM Triangle
)
SELECT x, y, z,
  CASE 
    WHEN xy_gt_z AND yz_gt_x AND zx_gt_y THEN 'Yes'
    ELSE 'No'
  END AS triangle
FROM sides;

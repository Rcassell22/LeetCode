/*
Problem:

Write an SQL query to report for every three line segments whether they can form a triangle.

Return the result table in any order.

Output:
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+

*/

-- Schema:
Create table If Not Exists Triangle (x int, y int, z int);
Truncate table Triangle;
insert into Triangle (x, y, z) values (13, 15, 30);
insert into Triangle (x, y, z) values (10, 20, 15);


-- Query:
SELECT x, y, z,
CASE
    WHEN SUM(x + y) > z AND SUM(y + z) > x AND SUM(x + z) > y THEN 'Yes'
    ELSE 'No'
END AS triangle
FROM Triangle
GROUP BY x, y, z;
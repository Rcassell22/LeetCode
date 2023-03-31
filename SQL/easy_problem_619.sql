/*
Problem:

A single number is a number that appeared only once in the MyNumbers table.

Write an SQL query to report the largest single number. If there is no single number, report null.


+-----+
| num |
+-----+
| 6   |
+-----+
*/

-- Schema:
Create table If Not Exists MyNumbers (num int);
Truncate table MyNumbers;
insert into MyNumbers (num) values (8);
insert into MyNumbers (num) values (8);
insert into MyNumbers (num) values (3);
insert into MyNumbers (num) values (3);
insert into MyNumbers (num) values (1);
insert into MyNumbers (num) values (4);
insert into MyNumbers (num) values (5);
insert into MyNumbers (num) values (6);

-- Query:
SELECT MAX(mn.num) as num
FROM (
    SELECT
        CASE
            WHEN count(num) = 1 THEN num
            ELSE NULL
    END as num
    FROM MyNumbers
    GROUP BY num
) as mn;
/*
Problem:

We define query quality as:

    The average of the ratio between query rating and its position.

We also define poor query percentage as:

    The percentage of all queries with rating less than 3.

Write an SQL query to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order.

Output:
+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog        | 2.50    | 33.33                 |
| Cat        | 0.66    | 33.33                 |
+------------+---------+-----------------------+

*/

-- Schema:
Create table If Not Exists Queries (query_name varchar(30), result varchar(50), position int, rating int);
Truncate table Queries;
insert into Queries (query_name, result, position, rating) values ('Dog', 'Golden Retriever', 1, 5);
insert into Queries (query_name, result, position, rating) values ('Dog', 'German Shepherd', 2, 5);
insert into Queries (query_name, result, position, rating) values ('Dog', 'Mule', 200, 1);
insert into Queries (query_name, result, position, rating) values ('Cat', 'Shirazi', 5, 2);
insert into Queries (query_name, result, position, rating) values ('Cat', 'Siamese', 3, 3);
insert into Queries (query_name, result, position, rating) values ('Cat', 'Sphynx', 7, 4);

-- Query:
-- This was the only solution I got working. I even tried some other peoples solutions and they were giving incorrect results.
-- I'm sure there's a better way to do this, I'll revist this another time.
WITH query_cte AS (
    SELECT q.query_name, count(q.query_name) as total, (SUM((CAST(q.rating AS DECIMAL) / CAST(q.position AS DECIMAL))) / count(q.query_name)) as div_result
    FROM Queries q
    GROUP BY q.query_name)
SELECT DISTINCT q.query_name, ROUND(qa.div_result, 2) AS quality, ROUND(qb.percent, 2) AS poor_query_percentage
FROM Queries q
INNER JOIN query_cte qa ON q.query_name = qa.query_name
INNER JOIN (
    SELECT q.query_name, ROUND(SUM(CASE WHEN q.rating < 3 THEN 1 ELSE 0 END) * 100 / COUNT(*), 2) AS percent
    FROM Queries q
    INNER JOIN query_cte qa ON q.query_name = qa.query_name
    GROUP BY q.query_name) qb ON q.query_name = qb.query_name;

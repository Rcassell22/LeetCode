/*
Problem:

Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

*/

-- Schema:
Create table If Not Exists Weather (id int, recordDate date, temperature int);
Truncate table Weather;
insert into Weather (id, recordDate, temperature) values (1, '2015-01-01', 10);
insert into Weather (id, recordDate, temperature) values (2, '2015-01-02', 25);
insert into Weather (id, recordDate, temperature) values (3, '2015-01-03', 20);
insert into Weather (id, recordDate, temperature) values (4, '2015-01-04', 30);

-- Query:
-- MySQL syntax
-- Subquery beat 5%:
SELECT w.id 
FROM Weather w 
WHERE w.temperature > (
	SELECT wa.temperature 
	FROM weather wa 
	WHERE wa.recordDate = (SELECT DATE_SUB(w.recordDate, INTERVAL 1 DAY))
);

-- Join beat 93%: 
SELECT w.id 
FROM Weather w 
INNER JOIN Weather wa ON wa.recordDate = (SELECT DATE_SUB(w.recordDate, INTERVAL 1 DAY))
WHERE w.temperature > wa.temperature;
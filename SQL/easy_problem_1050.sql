/*
Problem:

Write a SQL query for a report that provides the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

Return the result table in any order.


Output: 
+-------------+-------------+
| actor_id    | director_id |
+-------------+-------------+
| 1           | 1           |
+-------------+-------------+
*/

-- Schema:
Create table If Not Exists ActorDirector (actor_id int, director_id int, timestamp int);
Truncate table ActorDirector;
insert into ActorDirector (actor_id, director_id, timestamp) values (1, 1, 0);
insert into ActorDirector (actor_id, director_id, timestamp) values (1, 1, 1);
insert into ActorDirector (actor_id, director_id, timestamp) values (1, 1, 2);
insert into ActorDirector (actor_id, director_id, timestamp) values (1, 2, 3);
insert into ActorDirector (actor_id, director_id, timestamp) values (1, 2, 4);
insert into ActorDirector (actor_id, director_id, timestamp) values (2, 1, 5);
insert into ActorDirector (actor_id, director_id, timestamp) values (2, 1, 6);


-- Query:
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING count(*) >= 3;

-- HAVING is used when you need to use an aggregate function in a WHERE clause.
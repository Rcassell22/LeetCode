/*
Problem:

Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively.
A user was active on someday if they made at least one activity on that day.

Return the result table in any order.

Output:
+------------+--------------+
| day        | active_users |
+------------+--------------+
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |
+------------+--------------+

*/

-- Schema:
-- Had to modify ENUM type usage for PSQL
CREATE TYPE activity_enum AS ENUM('open_session', 'end_session', 'scroll_down', 'send_message');
Create table If Not Exists Activity (user_id int, session_id int, activity_date date, activity_type activity_enum);
Truncate table Activity;
insert into Activity (user_id, session_id, activity_date, activity_type) values (1, 1, '2019-07-20', 'open_session');
insert into Activity (user_id, session_id, activity_date, activity_type) values (1, 1, '2019-07-20', 'scroll_down');
insert into Activity (user_id, session_id, activity_date, activity_type) values (1, 1, '2019-07-20', 'end_session');
insert into Activity (user_id, session_id, activity_date, activity_type) values (2, 4, '2019-07-20', 'open_session');
insert into Activity (user_id, session_id, activity_date, activity_type) values (2, 4, '2019-07-21', 'send_message');
insert into Activity (user_id, session_id, activity_date, activity_type) values (2, 4, '2019-07-21', 'end_session');
insert into Activity (user_id, session_id, activity_date, activity_type) values (3, 2, '2019-07-21', 'open_session');
insert into Activity (user_id, session_id, activity_date, activity_type) values (3, 2, '2019-07-21', 'send_message');
insert into Activity (user_id, session_id, activity_date, activity_type) values (3, 2, '2019-07-21', 'end_session');
insert into Activity (user_id, session_id, activity_date, activity_type) values (4, 3, '2019-06-25', 'open_session');
insert into Activity (user_id, session_id, activity_date, activity_type) values (4, 3, '2019-06-25', 'end_session');

-- Query:
SELECT a.activity_date AS day, count(DISTINCT a.user_id) as active_users
FROM Activity a
WHERE a.activity_date > '2019-06-27' AND a.activity_date <= '2019-07-27'
GROUP BY activity_date;
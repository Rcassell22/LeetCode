/*
Write an SQL query to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
*/

-- Schema: 
Create table If Not Exists Person (id int, email varchar(255));
Truncate table Person;
insert into Person (id, email) values (1, 'a@b.com');
insert into Person (id, email) values (2, 'c@d.com');
insert into Person (id, email) values (3, 'a@b.com');

-- Query:
SELECT DISTINCT p.email AS Email 
FROM person p 
WHERE (
	SELECT count(pt.email) FROM person pt WHERE pt.email = p.email
) > 1;
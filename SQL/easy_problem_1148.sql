/*
Problem:

Write an SQL query to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

Output:
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
*/

-- Schema:
Create table If Not Exists Views (article_id int, author_id int, viewer_id int, view_date date);
Truncate table Views;
insert into Views (article_id, author_id, viewer_id, view_date) values (1, 3, 5, '2019-08-01');
insert into Views (article_id, author_id, viewer_id, view_date) values (1, 3, 6, '2019-08-02');
insert into Views (article_id, author_id, viewer_id, view_date) values (2, 7, 7, '2019-08-01');
insert into Views (article_id, author_id, viewer_id, view_date) values (2, 7, 6, '2019-08-02');
insert into Views (article_id, author_id, viewer_id, view_date) values (4, 7, 1, '2019-07-22');
insert into Views (article_id, author_id, viewer_id, view_date) values (3, 4, 4, '2019-07-21');
insert into Views (article_id, author_id, viewer_id, view_date) values (3, 4, 4, '2019-07-21');

-- Query:
SELECT DISTINCT v.author_id AS id
FROM Views v
WHERE v.author_id = v.viewer_id
GROUP BY v.article_id, v.author_id
ORDER BY v.author_id ASC;
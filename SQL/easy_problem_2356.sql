/*
Problem:

Write an SQL query to report the number of unique subjects each teacher teaches in the university.

Return the result table in any order.

+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
*/

-- Schema:
CREATE TABLE IF NOT EXISTS Teacher (teacher_id int, subject_id int, dept_id int);
TRUNCATE TABLE Teacher;
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (1, 2, 3);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (1, 2, 4);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (1, 3, 3);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (2, 1, 1);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (2, 2, 1);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (2, 3, 1);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (2, 4, 1);

-- Query:
SELECT t.teacher_id, count(*) as cnt
FROM (SELECT DISTINCT subject_id, teacher_id
FROM teacher) as t
GROUP BY teacher_id;

/*
Problem:

Write an SQL query to report all the classes that have at least five students.

Return the result table in any order.

*/


-- Schema:
Create table If Not Exists Courses (student varchar(255), class varchar(255));
Truncate table Courses;
insert into Courses (student, class) values ('A', 'Math');
insert into Courses (student, class) values ('B', 'English');
insert into Courses (student, class) values ('C', 'Math');
insert into Courses (student, class) values ('D', 'Biology');
insert into Courses (student, class) values ('E', 'Math');
insert into Courses (student, class) values ('F', 'Computer');
insert into Courses (student, class) values ('G', 'Math');
insert into Courses (student, class) values ('H', 'Math');
insert into Courses (student, class) values ('I', 'Math');

-- Query:
WITH cte_class_student_count(class, student_count) AS (
	SELECT class, count(class) AS student_count
	FROM Courses
	GROUP BY class
)
SELECT class
FROM cte_class_student_count
WHERE student_count >= 5;
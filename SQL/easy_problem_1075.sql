/*
Problem:

Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

Return the result table in any order.


Output:
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
*/

-- Schema:
Create table If Not Exists Project (project_id int, employee_id int);
Create table If Not Exists Employee (employee_id int, name varchar(10), experience_years int);
Truncate table Project;
insert into Project (project_id, employee_id) values (1, 1);
insert into Project (project_id, employee_id) values (1, 2);
insert into Project (project_id, employee_id) values (1, 3);
insert into Project (project_id, employee_id) values (2, 1);
insert into Project (project_id, employee_id) values (2, 4);
Truncate table Employee;
insert into Employee (employee_id, name, experience_years) values (1, 'Khaled', 3);
insert into Employee (employee_id, name, experience_years) values (2, 'Ali', 2);
insert into Employee (employee_id, name, experience_years) values (3, 'John', 1);
insert into Employee (employee_id, name, experience_years) values (4, 'Doe', 2);

-- Query:
SELECT p.project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM Project p
INNER JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;
/*
Problem:

Write an SQL query to find the employees who earn more than their managers.

Return the result table in any order.

Output format: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
*/

--Schema:
Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int);
Truncate table Employee;
insert into Employee (id, name, salary, managerId) values (1, 'Joe', 70000, 3);
insert into Employee (id, name, salary, managerId) values (2, 'Henry', 80000, 4);
insert into Employee (id, name, salary) values (3, 'Sam', 60000);
insert into Employee (id, name, salary) values (4, 'Max', 90000);

--Query:

-- Subquery (beat 89%)
SELECT e.name AS Employee FROM employee e WHERE e.salary > (SELECT et.salary FROM employee et WHERE et.id = e.managerId);

-- Self Join (only beat 24%)
SELECT e.name AS Employee FROM employee e
INNER JOIN employee et ON e.managerId = et.id
WHERE e.salary > et.salary;
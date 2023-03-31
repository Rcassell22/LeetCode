/*
Problem:

Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.

Return the result table in any order.

Output:
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+

*/


-- Schema:
Create table If Not Exists Employee (empId int, name varchar(255), supervisor int, salary int);
Create table If Not Exists Bonus (empId int, bonus int);
Truncate table Employee;
insert into Employee (empId, name, salary) values (3, 'Brad', 4000);
insert into Employee (empId, name, supervisor, salary) values (1, 'John', 3, 1000);
insert into Employee (empId, name, supervisor, salary) values (2, 'Dan', 3, 2000);
insert into Employee (empId, name, supervisor, salary) values (4, 'Thomas', 3, 4000);
Truncate table Bonus;
insert into Bonus (empId, bonus) values (2, 500);
insert into Bonus (empId, bonus) values (4, 2000);

-- Query:
-- Subquery (beat 74%)
SELECT e.Name, b.Bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000
OR e.empId NOT IN (SELECT ba.empId FROM Bonus ba);

-- No subquery (beat 62%)
SELECT e.Name, b.Bonus
FROM Employee e
LEFT OUTER JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
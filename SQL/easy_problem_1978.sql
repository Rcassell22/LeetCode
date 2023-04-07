/*
Problem:

Write an SQL query to report the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

Return the result table ordered by employee_id.


Output:
+-------------+
| employee_id |
+-------------+
| 11          |
+-------------+

*/

-- Schema:
CREATE TABLE IF NOT EXISTS Employees (employee_id INTEGER, name VARCHAR(20), manager_id INTEGER, salary INTEGER);
TRUNCATE TABLE Employees;
INSERT INTO Employees (employee_id, name, manager_id, salary) VALUES (3, 'Mila', 9, 60301);
INSERT INTO Employees (employee_id, name, manager_id, salary) VALUES (12, 'Antonella', NULL, 31000);
INSERT INTO Employees (employee_id, name, manager_id, salary) VALUES (13, 'Emery', NULL, 67084);
INSERT INTO Employees (employee_id, name, manager_id, salary) VALUES (1, 'Kalel', 11, 21241);
INSERT INTO Employees (employee_id, name, manager_id, salary) VALUES (9, 'Mikaela', NULL, 50937);
INSERT INTO Employees (employee_id, name, manager_id, salary) VALUES (11, 'Joziah', 6, 28485);

-- Query:
SELECT employee_id
FROM Employees
WHERE salary < 30000 AND manager_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id ASC;
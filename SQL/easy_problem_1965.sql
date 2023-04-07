/*
Problem:

Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:

The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.

Output:
+-------------+
| employee_id |
+-------------+
| 1           |
| 2           |
+-------------+

*/

-- Schema:
CREATE TABLE IF NOT EXISTS Employees (
  employee_id INT,
  name VARCHAR(30)
);
CREATE TABLE IF NOT EXISTS Salaries (
  employee_id INT,
  salary INT
);
TRUNCATE TABLE Employees;
INSERT INTO Employees (employee_id, name) VALUES
('2', 'Crew'),
('4', 'Haven'),
('5', 'Kristian');
TRUNCATE TABLE Salaries;
INSERT INTO Salaries (employee_id, salary) VALUES
('5', '76071'),
('1', '22517'),
('4', '63539');

-- Query:
SELECT e.employee_id
FROM (
    SELECT e.employee_id
    FROM Employees e
    LEFT JOIN Salaries s ON e.employee_id = s.employee_id
    UNION
    SELECT s.employee_id
    FROM Employees e
    RIGHT JOIN Salaries s ON e.employee_id = s.employee_id
) e
WHERE e.employee_id NOT IN (SELECT employee_id FROM Salaries)
OR e.employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id ASC;






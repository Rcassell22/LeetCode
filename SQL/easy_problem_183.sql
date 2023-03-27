/*
Problem:

Write an SQL query to report all customers who never order anything.

Return the result table in any order.

Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
*/

-- Schema:
Create table If Not Exists Customers (id int, name varchar(255));
Create table If Not Exists Orders (id int, customerId int);
Truncate table Customers;
insert into Customers (id, name) values (1, 'Joe');
insert into Customers (id, name) values (2, 'Henry');
insert into Customers (id, name) values (3, 'Sam');
insert into Customers (id, name) values (4, 'Max');
Truncate table Orders;
insert into Orders (id, customerId) values (1, 3);
insert into Orders (id, customerId) values (2, 1);

-- Query:
-- Sub Query (beat 39%) 
SELECT c.name AS Customers
FROM customers c 
WHERE c.id NOT IN (SELECT o.customerId FROM orders o);

-- Join (beat 73%)
SELECT c.name AS customers 
FROM customers c 
LEFT JOIN orders o ON c.id = o.customerId 
WHERE o.customerId IS NULL;
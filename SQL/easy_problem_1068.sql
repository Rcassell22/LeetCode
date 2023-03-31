/*
Problem:

Write an SQL query that reports the product_name, year, and price for each sale_id in the Sales table.

Return the resulting table in any order.

Output:
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+

*/

-- Schema:
Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int);
Create table If Not Exists Product (product_id int, product_name varchar(10));
Truncate table Sales;
insert into Sales (sale_id, product_id, year, quantity, price) values (1, 100, 2008, 10, 5000);
insert into Sales (sale_id, product_id, year, quantity, price) values (2, 100, 2009, 12, 5000);
insert into Sales (sale_id, product_id, year, quantity, price) values (7, 200, 2011, 15, 9000);
Truncate table Product;
insert into Product (product_id, product_name) values (100, 'Nokia');
insert into Product (product_id, product_name) values (200, 'Apple');
insert into Product (product_id, product_name) values (300, 'Samsung');

-- Query:
SELECT p.product_name, s.year, s.price
FROM Product p
INNER JOIN Sales s ON p.product_id = s.product_id;

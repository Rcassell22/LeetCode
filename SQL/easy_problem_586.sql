/*
Problem:

Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

Output: 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+

*/

-- Schema:
Create table If Not Exists orders (order_number int, customer_number int);
Truncate table orders;
insert into orders (order_number, customer_number) values (1, 1);
insert into orders (order_number, customer_number) values (2, 2);
insert into orders (order_number, customer_number) values (3, 3);
insert into orders (order_number, customer_number) values (4, 3);

-- Query:
WITH cte_customer_order_totals(customer_number, order_count) AS (
	SELECT customer_number, count(customer_number) AS order_count 
	FROM Orders
	GROUP BY customer_number
	ORDER BY order_count DESC
)
SELECT customer_number FROM cte_customer_order_totals LIMIT 1;
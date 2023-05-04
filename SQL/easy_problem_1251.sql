/*
Problem:

Write an SQL query to find the average selling price for each product. average_price should be rounded to 2 decimal places.

Return the result table in any order.

Output:
+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+

*/

-- Schema:
-- Using GPT 3.5 to convert Leetcode's poor quality set up scripts into PSQL.
CREATE TABLE IF NOT EXISTS Prices (
    product_id integer,
    start_date date,
    end_date date,
    price integer
);
CREATE TABLE IF NOT EXISTS UnitsSold (
    product_id integer,
    purchase_date date,
    units integer
);
TRUNCATE TABLE Prices;
INSERT INTO Prices (product_id, start_date, end_date, price)
VALUES (1, '2019-02-17', '2019-02-28', 5),
       (1, '2019-03-01', '2019-03-22', 20),
       (2, '2019-02-01', '2019-02-20', 15),
       (2, '2019-02-21', '2019-03-31', 30);
TRUNCATE TABLE UnitsSold;
INSERT INTO UnitsSold (product_id, purchase_date, units)
VALUES (1, '2019-02-25', 100),
       (1, '2019-03-01', 15),
       (2, '2019-02-10', 200),
       (2, '2019-03-22', 30);

-- Query:
SELECT p.product_id, ROUND(SUM(us.units * p.price) / SUM(units), 2) AS average_price
FROM Prices p
INNER JOIN UnitsSold us ON p.product_id = us.product_id
WHERE us.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;

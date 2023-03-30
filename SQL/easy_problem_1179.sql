/*
Problem:

Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

Return the result table in any order.

Output:
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+


Worst problem so far. I get the point but they could have just done one or two months.
*/

-- Schema:
Create table If Not Exists Department (id int, revenue int, month varchar(5));
Truncate table Department;
insert into Department (id, revenue, month) values (1, 8000, 'Jan');
insert into Department (id, revenue, month) values (2, 9000, 'Jan');
insert into Department (id, revenue, month) values (3, 10000, 'Feb');
insert into Department (id, revenue, month) values (1, 7000, 'Feb');
insert into Department (id, revenue, month) values (1, 6000, 'Mar');


-- Query:
SELECT id,
sum(CASE
    WHEN month = 'Jan' THEN revenue
    ELSE null
END) AS Jan_Revenue,
sum(CASE
    WHEN month = 'Feb' THEN revenue
    ELSE null
END) AS Feb_Revenue,
sum(CASE
    WHEN month = 'Mar' THEN revenue
    ELSE null
END) AS Mar_Revenue,
sum(CASE
    WHEN month = 'Apr' THEN revenue
    ELSE null
END) AS Apr_Revenue,
sum(CASE
    WHEN month = 'May' THEN revenue
    ELSE null
END) AS May_Revenue,
sum(CASE
    WHEN month = 'Jun' THEN revenue
    ELSE null
END) AS Jun_Revenue,
sum(CASE
    WHEN month = 'Jul' THEN revenue
    ELSE null
END) AS Jul_Revenue,
sum(CASE
    WHEN month = 'Aug' THEN revenue
    ELSE null
END) AS Aug_Revenue,
sum(CASE
    WHEN month = 'Sep' THEN revenue
    ELSE null
END) AS Sep_Revenue,
sum(CASE
    WHEN month = 'Oct' THEN revenue
    ELSE null
END) AS Oct_Revenue,
sum(CASE
    WHEN month = 'Nov' THEN revenue
    ELSE null
END) AS Nov_Revenue,
sum(CASE
    WHEN month = 'Dec' THEN revenue
    ELSE null
END) AS Dec_Revenue
FROM Department
GROUP BY id
ORDER BY id
/*
Problem:

Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. 
Note that you are supposed to write a DELETE statement and not a SELECT one.
After running your script, the answer shown is the Person table. 
The driver will first compile and run your piece of code and then show the Person table. 
The final order of the Person table does not matter.

*/

-- Schema:
Create table If Not Exists Person (Id int, Email varchar(255));
Truncate table Person;
insert into Person (id, email) values (1, 'john@example.com');
insert into Person (id, email) values (2, 'bob@example.com');
insert into Person (id, email) values (3, 'john@example.com');

-- Query:
DELETE FROM Person WHERE id IN (
SELECT pb.id
FROM (
        SELECT pa.id, row_number() OVER (PARTITION BY pa.email ORDER BY pa.id) as rn FROM person pa
) pb WHERE pb.rn > 1);
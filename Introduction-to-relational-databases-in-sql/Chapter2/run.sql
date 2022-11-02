-- Section1: Types of database constraints
/*
A: SQL aggregate functions

-- Section2: Conforming with data types
-- Let's add a record to the table
INSERT INTO transactions (transaction_date, amount, fee)
VALUES ('2018-09-24', 5454, '30');
-- Doublecheck the contents
SELECT *
FROM transactions;

-- Section3: Type CASTs
-- Calculate the net amount as amount + fee
SELECT transaction_date, amount + CAST(fee AS integer) AS net_amount
FROM transactions;

-- Section4: Change types with ALTER COLUMN
-- Select the university_shortname column
SELECT DISTINCT(university_shortname)
FROM professors;
//////////////////////////////////////
-- Specify the correct fixed-length character type
ALTER TABLE professors
ALTER COLUMN university_shortname
TYPE char(3);
//////////////////////////////////////
-- Change the type of firstname
ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(64);

-- Section5: Convert types USING a function
-- Convert the values in firstname to a max. of 16 characters
ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(16)
USING SUBSTRING(firstname from 1 FOR 16);
SELECT firstname
FROM professors;
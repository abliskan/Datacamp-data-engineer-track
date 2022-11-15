-- Section1: Create a role
/*
-- Create a data scientist role
CREATE ROLE data_scientist;
-- ////////////////////
-- Create a role for Marta
CREATE ROLE marta LOGIN;
-- ////////////////////
-- Create an admin role
CREATE ROLE admin WITH CREATEDB CREATEROLE;

-- Section2: Grant privileges and alter attributes
-- Grant data_scientist update and insert privileges
GRANT UPDATE, INSERT ON long_reviews TO data_scientist;
-- Give Marta's role a password
ALTER ROLE marta WITH PASSWORD 's3cur3p@ssw0rd';

-- Section3: Add a user role to a group role
-- Add Marta to the data scientist group
GRANT data_scientist TO marta;
-- Celebrate! You hired data scientists.
-- Remove Marta from the data scientist group
REVOKE data_scientist FROM marta;

-- Section4: Reasons to partition
A: Improve data integrity

-- Section5: Partitioning and normalization
+ Normalization
- Reduce redundancy in table
- Changes the logical data model

+ Vertical Partitioning
- Move specific columns to slower medium
- (Example) Move the third and fourth column to separate table

+ Horizontal Partitioning
- Sharding is an extension on this, using multiple machines
- (Example) Use the timestamp to move rows from Q4 in a specific table

-- Section6: Creating vertical partitions
-- Create a new table called film_descriptions
CREATE TABLE film_descriptions (
    film_id INT,
    long_description TEXT
);
-- Copy the descriptions from the film table
INSERT INTO film_descriptions
SELECT film_id, long_description FROM film;
-- ////////////////////
-- Create a new table called film_descriptions
CREATE TABLE film_descriptions (
    film_id INT,
    long_description TEXT
);
-- Copy the descriptions from the film table
INSERT INTO film_descriptions
SELECT film_id, long_description FROM film;
    -- Drop the descriptions from the original table
ALTER TABLE film DROP COLUMN long_description;
-- Join to view the original table
SELECT * FROM film
JOIN film_descriptions USING(film_id);

-- Section7: Creating horizontal partitions
-- Create a new table called film_partitioned
CREATE TABLE film_partitioned (
  film_id INT,
  title TEXT NOT NULL,
  release_year TEXT
)
PARTITION BY LIST (release_year);
-- ////////////////////
-- Create a new table called film_partitioned
CREATE TABLE film_partitioned (
  film_id INT,
  title TEXT NOT NULL,
  release_year TEXT
)
PARTITION BY LIST (release_year);
-- Create the partitions for 2019, 2018, and 2017
CREATE TABLE film_2019
	PARTITION OF film_partitioned FOR VALUES IN ('2019');

CREATE TABLE film_2018
	PARTITION OF film_partitioned FOR VALUES IN ('2018');

CREATE TABLE film_2017
	PARTITION OF film_partitioned FOR VALUES IN ('2017');
-- ////////////////////
-- Create a new table called film_partitioned
CREATE TABLE film_partitioned (
  film_id INT,
  title TEXT NOT NULL,
  release_year TEXT
)
PARTITION BY LIST (release_year);
-- Create the partitions for 2019, 2018, and 2017
CREATE TABLE film_2019
	PARTITION OF film_partitioned FOR VALUES IN ('2019');

CREATE TABLE film_2018
	PARTITION OF film_partitioned FOR VALUES IN ('2018');

CREATE TABLE film_2017
	PARTITION OF film_partitioned FOR VALUES IN ('2017');
-- Insert the data into film_partitioned
INSERT INTO film_partitioned
SELECT film_id, title, release_year FROM film;
-- View film_partitioned
SELECT * FROM film_partitioned;

-- Section8: Data integration do's an don't
+ False
- Automated testing and proactive alerts are not needed
- You should choose whichever solution is right for the job right now
- All your data has to be updated in real time in the final view
- Your data integration solution, hand-coded or ETL tool, should work once and then you can use the resulting view to run queries forever
- Everybody should have access to sensitive data in the final view
- After data integration all your data should be in a single table
+ True
- Being able to access the desired data through a single view does not mean all data is sotred together
- My source data can be in different formats and database management systems
- My source data can be stored in different physical locations
- Data integration should be business driven, e.g. what combination of data will be useful for the business
- Data in the final view can be updated in different intervals
- You should be careful choosing a hand-coded solution because of maintenance cost

-- Section9: Analyzing a data integration plan
A: You should indicate that you plan to anonymize patient health records.

-- Section10: SQL versus NoSQL
A: You are concerned about data consistency and 100% data integrity is your top goal.

-- Section11: Choosing the right DBMS
+ SQL
- A banking application where it's extremely important that data integrity is ensured.

+ NoSQL
- A social media tool that provides users with the opportunities to gorw their networks via connections.
- During the holiday shopping season, an e-commerce website needs to keep track of millions of shopping carts.
- Data warehousing on big data.
- A blog that needs to create and incorporate new types of content, such as images, comments, and videos.
*/
-- Section1: OLAP vs OLTP
/*
OLAP
+ Helps business with decision making and problem solving
+ Queries a larger amount of data
+ Typically uses a data warehouse
OLTP
+ Data is inserted and updated more often
+ Most likely to have data from the past hour
+ Typically uses an operational database

-- Section2: Which is better?
A: OLTP because this table's structure appears to require frequent updates.

-- Section3: Name that data type!
Unstructured
+ Images in your photo libray
+ Zip file of all text messages ever received
+ To-do notes in a text editor
Semi-Structured
+ CSV of open data downloaded from your local goverment websites
+ JSON object of tweets outputted in real-time by the twitter API
Structured
+ A relational database with latest withdrawals and deposits made by clients

-- Section4: Ordering ETL Task
- eCommerce API outputs real time data of transactions
- Python script drops null rows and clean data into pre-determined columns
- Resulting dataframe is written into an AWS Redshift Warehouse

-- Section5: Recommend a storage solution
A: To create accessible and isolated data repositories for other analysts

-- Section6: Classifying data models
Conceptual Data Model
+ Entities, attributes, and relationships
+ Gathers business requirements
Logical Data Model
+ Relational model
+ Determining tables and columns
Physical Data Model
+ File structure of data storage

-- Section7: Deciding fact and dimension tables
A: A fact table holding duration_mins and foreign keys to dimension tables holding route details and week details, respectively.
-- //////////////////
-- Create a route dimension table
CREATE TABLE route(
	route_id INTEGER PRIMARY KEY,
    park_name VARCHAR(160) NOT NULL,
    city_name VARCHAR(160) NOT NULL,
    distance_km FLOAT NOT NULL,
    route_name VARCHAR(160) NOT NULL
);
-- Create a week dimension table
CREATE TABLE week (
	week_id INTEGER PRIMARY KEY,
    week INTEGER NOT NULL,
    month VARCHAR(160) NOT NULL,
    year INTEGER NOT NULL
);

-- Section8: Querying the dimensional model
SELECT
	-- Select the sum of the duration of all runs
	SUM(duration_mins)
FROM
	runs_fact;
-- //////////////////
SELECT
	-- Get the total duration of all runs
	SUM(duration_mins)
FROM
	runs_fact
-- Get all the week_id's that are from July, 2019
INNER JOIN week_dim ON week_dim.week_id = runs_fact.week_id
WHERE week_dim.month = 'July' and week_dim.year = '2019';
*/
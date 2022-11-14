-- Section1: Tables vs Views
/*
+ Only tables
- Part of the physical schema of a database

+ Views & tables
- Contains rows and columns
- Can be queried
- Has access control

+ Only views
- Takes up less memory
- Always defined by a query

-- Section2: Viewing views
-- Get all non-systems views
SELECT * FROM information_schema.views
WHERE table_schema NOT IN ('pg_catalog', 'information_schema');
-- ////////////////////
Returns the content records that have reviews of more than 4000 characters.
-- ////////////////////
Returns the top 10 highest scored reviews published in 2017.

-- Section2: Viewing views
-- Get all non-systems views
SELECT * FROM information_schema.views
WHERE table_schema NOT IN ('pg_catalog', 'information_schema');
-- ////////////////////
A: Returns the content records that have reviews of more than 4000 characters.
-- ////////////////////
A: Returns the top 10 highest scored reviews published in 2017.

-- Section3: Creating and querying a view
-- Create a view for reviews with a score above 9
CREATE VIEW high_scores AS
SELECT * FROM reviews
WHERE score > 9;
-- ////////////////////
-- Create a view for reviews with a score above 9
CREATE VIEW high_scores AS
SELECT * FROM REVIEWS
WHERE score > 9;
-- Count the number of self-released works in high_scores
SELECT COUNT(*) FROM high_scores
INNER JOIN labels ON labels.reviewid = high_scores.reviewid
WHERE label = 'self-released';

-- Section4: Creating a view from other views
-- Create a view with the top artists in 2017
CREATE VIEW top_artists_2017 AS
-- with only one column holding the artist field
SELECT artist_title.artist FROM artist_title
INNER JOIN top_15_2017
ON top_15_2017.reviewid = artist_title.reviewid;
-- Output the new view
SELECT * FROM top_artists_2017;
-- ////////////////////
A: DROP VIEW top_15_2017 CASCADE;

-- Section5: Granting and revoking access
-- Revoke everyone's update and insert privileges
REVOKE UPDATE, INSERT ON long_reviews FROM PUBLIC;
-- Grant the editor update and insert privileges
GRANT UPDATE, INSERT ON long_reviews TO editor;

-- Section6: Updatable views
A: long_reviews

-- Section7: Redefining a view
A: Yes, as long as the label column comes at the end.
-- ////////////////////
-- Redefine the artist_title view to have a label column
CREATE OR REPLACE view artist_title AS
SELECT reviews.reviewid, reviews.title, artists.artist, labels.label
FROM reviews
INNER JOIN artists
ON artists.reviewid = reviews.reviewid
INNER JOIN labels
ON labels.reviewid = reviews.reviewid;

SELECT * FROM artist_title;

-- Section8: Materialized versus non-materialized
+ Non-Materialized Views
- Always returns up-to-date data
- Better to use on write-intensive databases

+ Non-Materialized & Materialized Views
- Helps reduce the overhead of writing queries
- Can be used in a data warehouse

+ Materialized Views
- Consumes more storage
- Stores the query result on disk

-- Section9: Creating and refreshing a materialized view
-- Create a materialized view called genre_count
CREATE materialized VIEW genre_count AS
SELECT genre, COUNT(*)
FROM genres
GROUP BY genre;

INSERT INTO genres
VALUES (50000, 'classical');

-- Refresh genre_count
REFRESH materialized VIEW genre_count;

SELECT * FROM genre_count;
*/
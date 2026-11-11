-- Aggregate functions - calaculate one result from many rows
-- COUNT() - the number of rows
-- SUM() - total value
-- AVG() - average value
-- MIN() - smallest value
-- MAX() - largest value

SELECT
COUNT(*) AS total_posts
FROM basics.posts;

SELECT
COUNT(*) AS total_posts,
COUNT(*) FILTER (WHERE status = 'published') AS published_posts,
SUM(views) AS total_views,
AVG(views) AS average_views,
MAX(views) AS highest_views,
MIN(views) AS lowest_views
FROM basics.posts;

SELECT
-- COUNT(*) AS total_postss
COUNT(*) FILTER (WHERE status = 'draft') AS drafts
FROM basics.posts;
-- Left Join - keeps all rows from the left table.
-- PostgreSQL then returns matching data from the right table
-- When there is no matching data in th right table, PostgreSQL returns NULL

SELECT
basics.posts.title AS post_title,
basics.comments AS comment_body
FROM basics.posts
LEFT JOIN basics.comments
ON basics.comments.post_id = basics.posts.id
ORDER BY basics.posts.title;  
-- A many-to-many relationship between two tables exists when multiple records in one table are related to multiple records in another tables

-- In our example, one post can have multiple tags and a tag can used(associated with) multiple posts

-- posts.id == post_tags.post_id
-- tags.id == post_tags.tag_id

SELECT
basics.posts.title AS post_titlee,
basics.tags.name AS tag_name
FROM basics.posts
INNER JOIN basics.post_tags
ON basics.posts.id = basics.post_tags.post_id
INNER JOIN basics.tags
ON basics.post_tags.tag_id = basics.tags.id
ORDER BY basics.tags.name, basics.posts.title;

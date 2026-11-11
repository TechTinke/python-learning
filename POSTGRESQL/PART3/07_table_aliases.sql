-- Aliases - make queries shorter and easier to read

SELECT
p.title AS post_title,
p.status,
p.views,
u.name AS author_name,
c.body AS comment_body
FROM basics.posts AS p
INNER JOIN basics.users AS u
ON u.id = p.user_id
LEFT JOIN basics.comments as c 
ON c.post_id = p.id 
ORDER BY p.views DESC;

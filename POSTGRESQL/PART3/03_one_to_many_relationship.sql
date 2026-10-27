-- one parent row can have multiple child rows
-- In our example, one user can write many posts but a post will always belong to one user

-- users - parent table
-- posts - child table

-- posts.user_id points to users.id 

-- users.id is the original user id whie posts/user_id stores the original user id inside the posts table

-- show all the posts with all their owners
SELECT
basics.users.name AS author_name,
basics.posts.title AS post_title,
basics.posts.status
FROM basics.users
INNER JOIN basics.posts
    ON basics.users.id = basics.posts.user_id
ORDER  BY basics.users.name, basics.posts.title;

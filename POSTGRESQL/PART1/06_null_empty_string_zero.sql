-- null - unknown/missing value
-- empty string - known string value but contains no characters
-- zero - actual numeric value of 0

DROP TABLE IF EXISTS basics.value_examples;

CREATE TABLE basics.value_examples(
    id SERIAL PRIMARY KEY,

    nickname TEXT,

    bio TEXT,

    score INTEGER
);

INSERT INTO basics.value_examples (nickname, bio, score)
VALUES
(null, 'cheeky boy', 80),
('', 'empty nickname', 67),
('altonmaison', '', 0);

-- SELECT * FROM basics.value_examples
-- WHERE nickname IS NULL;

-- SELECT * FROM basics.value_examples
-- WHERE nickname = '';

-- SELECT * FROM basics.value_examples
-- WHERE score = 0;

SELECT * FROM basics.value_examples
WHERE nickname IS NOT NULL;



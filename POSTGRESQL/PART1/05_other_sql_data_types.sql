DROP TABLE IF EXISTS basics.app_events;

CREATE TABLE basics.app_events(
    -- UUID
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    event_name TEXT NOT NULL,

    -- JSONB
    metadata JSONB DEFAULT '{}' ::jsonb,

    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO basics.app_events(event_name, metadata)
VALUES
('sign_up','{"browser":"chrome"}'),
('sign_in', '{"username":"davis"}');

-- SELECT * FROM basics.app_events;

-- SELECT
--     event_name,
--     metadata ->> 'browser' AS browser 
--     -- Open JSON B column named metadata and get the value of browser as text
-- FROM basics.app_events
-- WHERE metadata ? 'browser';

SELECT
    event_name,
    metadata ->> 'username' AS username
FROM basics.app_events
WHERE metadata ? 'username';

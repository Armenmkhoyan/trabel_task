WITH cte AS
        (SELECT
            DISTINCT TOP 2000
            ua.user_id,
            ua.device_time
        FROM
            users_activity ua
        WHERE
            ua.device_time = {date}
        AND ua.user_id NOT IN (SELECT user_id FROM temp_users)
        AND ua.user_id IN (SELECT user_id
                                    FROM   users
                                    WHERE platform = 'iOS'
                                    AND os_version = '14'
                                    AND registered_at > DATEDIFF(SECOND, '19700101', '20240401')
                                    AND registered_at < DATEDIFF(SECOND, '19700101', '20240501')))
INSERT INTO sampled_activity_data
            (user_id,
             segment,
             screen_name,
             screen_action,
             device_time)
SELECT c.user_id,
       'SegmentB' AS SEGMENT,
       ua.screen_name,
       ua.screen_action,
       ua.device_time
FROM   cte AS c
    JOIN users_activity AS ua
        ON c.user_id = ua.user_id
        AND ua.device_time = c.device_time

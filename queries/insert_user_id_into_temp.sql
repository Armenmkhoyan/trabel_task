insert into
    temp_users (user_id, device_time)
select
    distinct
    user_id,
    device_time
from
    sampled_activity_data
where
    device_time = {date}
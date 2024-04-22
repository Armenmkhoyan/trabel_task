import random
import time

import numpy as np

from patterns import *

actions_combinations = [
    [name, action] for name, actions in screen_name_action.items() for action in actions
]


def generate_user() -> list:

    start_ts = time.mktime(time.strptime(start_date, "%Y-%m-%d"))
    end_ts = time.mktime(time.strptime(end_date, "%Y-%m-%d"))
    country = np.random.choice(countries)
    platform = np.random.choice(["Android", "iOS"], p=[0.8, 0.2])
    registered_at = np.random.randint(start_ts, end_ts)
    device_brand = np.random.choice(phone_brands[platform])
    device_model = np.random.choice(phone_models[device_brand])
    library_size = np.random.randint(0, 5000)
    os_version = np.random.choice(platforms_versions[platform])

    return [
        country,
        platform,
        registered_at,
        device_model,
        device_brand,
        library_size,
        os_version,
    ]


def generate_users(n_users: int) -> list:
    start_ts = int(time.mktime(time.strptime(start_date, "%Y-%m-%d")))
    end_ts = int(time.mktime(time.strptime(end_date, "%Y-%m-%d")))

    countries_batch = np.random.choice(countries, n_users).tolist()
    platforms_batch = np.random.choice(["Android", "iOS"], p=[0.8, 0.2], size=n_users)
    registered_at_batch = np.random.randint(start_ts, end_ts, size=n_users).tolist()
    device_brands_batch = [
        np.random.choice(phone_brands[platform]) for platform in platforms_batch
    ]
    device_models_batch = [
        np.random.choice(phone_models[brand]) for brand in device_brands_batch
    ]
    library_sizes_batch = np.random.randint(0, 5000, size=n_users).tolist()
    os_versions_batch = [
        np.random.choice(platforms_versions[platform]) for platform in platforms_batch
    ]

    users_data = list(
        zip(
            countries_batch,
            platforms_batch,
            registered_at_batch,
            device_models_batch,
            device_brands_batch,
            library_sizes_batch,
            os_versions_batch,
        )
    )
    return users_data


def generate_event(batch_size: int, action_start_timestamp: int) -> list:
    user_action_list = []

    for _ in range(batch_size):
        user_id = np.random.randint(1, 100000000)
        num_actions = random.randint(1, len(screen_name_action))
        selected_actions = random.sample(actions_combinations, num_actions)

        for action in selected_actions:
            user_action_list.append([user_id] + action + [action_start_timestamp])

    return user_action_list

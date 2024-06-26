start_date = "2024-03-15"
end_date = "2024-05-15"

countries = [
    "US",
    "CA",
    "MX",
    "BR",
    "AR",
    "CO",
    "GB",
    "FR",
    "DE",
    "IT",
    "ES",
    "PL",
    "SE",
    "RU",
]
phone_brands = {"Android": ["Xiaomi", "Samsung"], "iOS": ["Iphone"]}
phone_models = {
    "Samsung": ["GalaxyS20", "GalaxyS21", "A20"],
    "Xiaomi": ["MI 13 Pro", "MI 14 Ultra", "MI 14 Pro"],
    "Iphone": ["15 Pro", "14 Pro", "13 Pro Max", "15 Pro Max"],
}
platforms_versions = {"Android": ["11", "12", "13"], "iOS": ["14", "15", "16"]}

screen_name_action = {
    "artist_page": [
        "share_button_click",
        "album_click",
        "back_button_click",
        "video_click",
        "download_top_songs_click",
        "add_list_button_click",
        "songs_list_click",
        "latest_release_click",
        "unfollow_click",
        "playlist_click",
    ],
    "forgot_password": ["send_login_link_click"],
    "gender_screen": ["skip_click", "selector_opened", "next_click"],
    "home": [
        "lists_list_click",
        "link_click",
        "song_list_click",
        "album_list_click",
        "page_click",
        "song_click",
        "artist_click",
        "playlist_click",
        "video_click",
        "album_click",
    ],
    "library": ["import_library_click"],
    "log_in": ["google_click", "fb_click", "email_click", "forgot_password_click"],
    "main_tap_bar": [
        "home_button_click",
        "list_button_click",
        "library_button_click",
        "discover_button_click",
        "search_button_click",
    ],
    "notifications": [
        "delete_notifications_click",
        "notification_settings_click",
        "back_button_click",
        "notification_click",
        "user_list_click",
        "read_all_click",
        "delete_all_notifications_click",
    ],
    "player": [
        "view_album_click",
        "add_to_queue_click",
        "next_button_click",
        "share_button_click",
        "pause_button_click",
        "back_button_click",
        "comment_click",
        "like_button_click",
        "previous_button_click",
        "lyrics_click",
    ],
    "search": [
        "ai_container_click",
        "album_click",
        "search_submit",
        "song_id_click",
        "artist_list_click",
        "album_list_click",
        "song_click",
        "search_bar_click",
        "artist_click",
        "link_click",
    ],
    "search_result": [
        "album_search_on_youtube_click",
        "artist_search_on_youtube_click",
        "song_search_on_youtube_click",
        "profile_chip_click",
        "lists_list_click",
        "albums_chip_click",
        "artist_list_click",
        "back_button_click",
        "all_search_on_youtube_click",
        "podcast_episode_click",
    ],
    "sign_up": [
        "privacy_policy_click",
        "email_click",
        "fb_click",
        "log_in_click",
        "google_click",
    ],
    "song_download_preview": ["download_button_click", "back_button_click"],
    "user_profile": [
        "playlist_click",
        "profile_visit_user_click",
        "playlist_downloaded_user_click",
        "followers_click",
        "fan_playlist_click",
        "follow_click",
        "share_button_click",
        "edit_profile_click",
        "following_click",
    ],
}

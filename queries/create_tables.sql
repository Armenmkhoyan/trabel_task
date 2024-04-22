
USE Trabel;
GO

IF OBJECT_ID('users', 'U') IS NULL
BEGIN
    CREATE TABLE users (
        user_id INT IDENTITY(1,1),
        country NVARCHAR(50),
        platform NVARCHAR(50),
        registered_at INT,
        device_model NVARCHAR(50),
        device_brand NVARCHAR(50),
        library_size INT,
        os_version NVARCHAR(50)
    );
END
GO

IF OBJECT_ID('users_activity', 'U') IS NULL
BEGIN
    CREATE TABLE users_activity (
        user_id INT,
        screen_name NVARCHAR(50),
        screen_action NVARCHAR(50),
        device_time INT
    );
END
GO

IF OBJECT_ID('sampled_activity_data', 'U') IS NULL
BEGIN
    CREATE TABLE sampled_activity_data (
        user_id INT,
        segment VARCHAR(50),
        screen_name NVARCHAR(50),
        screen_action NVARCHAR(50),
        device_time INT
    );
END

GO

IF OBJECT_ID('temp_users', 'U') IS NULL
BEGIN
    CREATE TABLE temp_users (
            user_id varchar(20),
            device_time int
    );
END

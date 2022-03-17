# DROP TABLES

song_table_drop = "DROP TABLE IF EXISTS songs_table"
artist_table_drop = "DROP TABLE IF EXISTS artists_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"
user_table_drop = "DROP TABLE IF EXISTS users_table"
songplay_table_drop = "DROP TABLE IF EXISTS songplays_table"




# CREATE TABLES

song_table_create = (
    """
    CREATE TABLE songs_table (
    song_id varchar PRIMARY KEY,
    title varchar NOT NULL,
    artist_id varchar NOT NULL,
    year int NOT NULL,
    duration numeric NOT NULL)
    """
)

artist_table_create = (
    """
    CREATE TABLE artists_table (
    artist_id varchar PRIMARY KEY,
    artist_name varchar NOT NULL,
    artist_location varchar NOT NULL,
    artist_latitude float,
    artist_longitude float)
    """
)

time_table_create = (
    """
    CREATE TABLE time_table (
    start_time timestamp PRIMARY KEY,
    hour int NOT NULL,
    day int NOT NULL,
    week int NOT NULL,
    month int NOT NULL,
    year int NOT NULL,
    weekday int NOT NULL)
    """
)

user_table_create = (
    """
    CREATE TABLE users_table (
    user_id int PRIMARY KEY,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    gender char(1) NOT NULL,
    level varchar NOT NULL)
    """
)

songplay_table_create = (
    """
    CREATE TABLE songplays_table (
    songplay_id serial PRIMARY KEY,
    start_time timestamp NOT NULL,
    user_id int NOT NULL,
    level varchar NOT NULL,
    song_id varchar,
    artist_id varchar,
    session_id int NOT NULL,
    location varchar NOT NULL,
    user_agent varchar NOT NULL)
    """
)



# INSERT RECORDS

song_table_insert = (
    """
    INSERT INTO songs_table (song_id, title, artist_id, year, duration) 
    VALUES(%s, %s, %s, %s, %s) 
    ON CONFLICT DO NOTHING
    """
)

artist_table_insert = (
    """
    INSERT INTO artists_table (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
    """
)

time_table_insert = (
    """INSERT INTO time_table (start_time, hour, day, week, month, year, weekday)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
    """
)

user_table_insert = (
    """INSERT INTO users_table (user_id, first_name, last_name, gender, level)
    VALUES(%s, %s, %s, %s, %s) \
    ON CONFLICT (user_id) DO NOTHING
    """
)
# ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level

songplay_table_insert = (
    """
    INSERT INTO songplays_table(
        start_time, user_id, level, song_id,
        artist_id, session_id, location, user_agent
        )
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s) 
    ON CONFLICT DO NOTHING
    """
)



# FIND SONGS

song_select = (
    """
    SELECT st.song_id, at.artist_id FROM songs_table AS st
    JOIN artists_table AS at
    ON st.artist_id = at.artist_id
    WHERE st.title = %s AND at.artist_name = %s AND st.duration = %s
    """
)



# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
import sqlite3
import pandas as pd

conn = sqlite3.connect('example.db')
cursor = conn.cursor() 

cursor.executescript("""
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Movie_Actor;

CREATE TABLE IF NOT EXISTS Movie(
    Movie_id INTEGR PRIMARY KEY,
    Title TEXT,
    Genre TEXT,
    Year INTEGER,
    Rating REAL,
    Duration INTEGER
);

CREATE TABLE IF NOT EXISTS Actor(
    Actor_id INTEGER PRIMARY KEY,
    Actor_name TEXT,
    Birth_year INTEGER,
    Country TEXT
);

CREATE TABLE IF NOT EXISTS Movie_Actor(
    Movie_id INTEGER,
    Actor_id INTEGER
);

INSERT INTO Movie VALUES     
    (1,'The Lion King','Animation',1994,8.5,88),
    (2,'Toy Story','Animation',1995,8.3,81),
    (3,'Frozen','Animation',2013,7.4,102),
    (4,'Moana',Animation',2016,7.6,107),
    (5,'Spider-Man','Action',2002,7.3,121),
    (6,'Black Panther','Action',2018,7.3,134),
    (7,'Avengers','Action',2012,8.0,143).
    (8,'Matilda','Drama',1996,7.0,98),
    (9,'Home Alone','Comedy',1990,7.7,103),
    (10,'Elf','Comedy',2003,6.9,97),
    (11,'Coco','Animation',2017,8.4,105),
    (12,'Interstellar','Drama',2014,8.6,169);

INSERT INTO Actor VALUES
    (1,'Tom Hanks',1956,'USA'),
    (2,'Idris Elba',1972,'UK'),
    (3,'Chadwick Boseman',1976,'USA'),
    (4,'Scarlet Johannson',1984,'USA'),
    (5,'Macaulay Culkin',1980,'USA'),
    (6,'Will Smith',1968,'USA'),
    (7,'Meryl Streep',1949,'USA'),
    (8,'Lupita Nyongo',1983,'Kenya'),
    (9,'Priyanka Chopra,'1982,'India'),
    (10,'Jackie Chan',1954,'China');

INSERT INTO Movie_Actor VALUES
    (1,2),(2,1),(5,1),(6,3),(6,8),(7,4),(8,7),(9,5),(11,2),(12,1);
""")
conn.commit()
print("Database ready!")

# ------------- Part 2: DISTINCT - Unique Value only ---------------
# DISTINCT removes duplicate values - only one copy of each
# unique value is returned. Use it to see what the differernt values in a column are, without repeats.

# All unique genres in the Movie Table
genres = pd.read_sql("""SELECT DISTINCT(Genre)
    FROM Movie;""", conn)
print(genres)

# All unique countries the actors come from
countries = pd.read_sql("""SELECT DISTINCT(Country)
    FROM Actor;""", conn)
print(countries)

# ----------- Part 3: ORDER BY - Sorting Results -------
# ORDER BY sorts th result by a chosen column
# Default order is ascending - smallest or earliest first
# Add DESC to filp it - largest or latest first

# All movies sorted by Rating - highest rated first
top_movies = pd.read_sql("""SELECT Title, Genre,Rating
    FROM Movie
    ORDER BY Rating DESC;""", conn)
print(top_movies)

oldest_first = pd.read_sql("""SELECT Title,Year
    FROM Movie
    ORDER BY Year;""", conn)
print(oldest_first)

youngest_actors = pd.read_sql("""SELECT Actor_name, Birth_year,Country
    FROM Actor
    ORDER BY Birth_year DESC;""", conn)
print(youngest_actors)

action_count = pd.read_sql("""SELECT COUNT(Movie_id)
    FROM Movie
    WHERE Genre == 'Action';""", conn)
print(action_count)

animation_mins = pd.read_sql("""SELECT SUM(Duration)
    FROM Movie
    WHERE Genre == 'Animation';""", conn)
print(animation_mins)

avg_rating = pd.read_sql("""SELECT AVG(Rating)
    FROM Movie;""", conn)
print(avg_rating)

avg_action_dur = pd.read_sql("""SELECT AVG(Duration)
    FROM Movie
    WHERE Genre == 'Action';""", conn)
print(avg_action_dur)

movies_per_genre = pd.read_sql("""SELECT Genre, COUNT(Movie_id)
    FROM Movie
    GROUP BY Genre;""", conn)
print(movies_per_genre)

avg_per_genre = pd.read_sql("""SELECT Genre, AVG(Rating)
    FROM Movie
    GROUP BY Genre
    ORDER BY AVG(Rating) DESC;""", conn)
print(avg_per_genre)

conn.close()
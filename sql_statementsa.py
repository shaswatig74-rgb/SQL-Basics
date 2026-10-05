# Activity 1

# ------- Part 1 : Build the Database
# sqlite3 lets Python create and read database files
# Here we go build a small cricket database with 3 tables
# Team, Match, and Player_Match - then connect to it

import sqlite3
import pandas as pd

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Team,
DROP TABLE IF EXISTS Match,
DROP TABLE IF EXISTS Player_Match;

CREATE TABLE Team(
    Team_id INTEGER PRIMARY KEY,
    Team_Name TEXT
);

CREATE TABLE Match(
    Match_id INTEGER PRIMARY KEY,
    Season_id INTEGER,
    Match_Winner INTEGER,
    Win_Margin INTEGER
);

CREATE TABLE Player_Match(
    Match_id INTEGER,
    Player_id INTEGER
);

INSERT INTO Team VALUES
    (1,'Chennai Super Kings'),(2,'Delhi Capitals'),
    (3, 'Deccan Chargers'),(4,'Delhi Daredevils'),
    (5,'Mumbai Indians'),(6,'Kolkata Night Riders'),
    (7,'Rajasthan Royals'),(8,'Kingas XI Punjab');

INSERT INTO Match VALUES
    (1,7,5,35),(2,7,5,22),(3,8,5,45),(4,8,5,8),
    (5,8,1,67),(6,8,6,19),(7,9,5,33),(8,9,1,28),
    (9,9,5,12),(10,9,6,55),(11,9,3,38),(12,9,7,4);

INSERT INTO Player_Match VALUES
    (1,101),(1,102),(2,103),(3,104),(4,105),(5,106);
""")

conn.commit()
print("Database ready!")

# Part 2: See All Tables in the Database
# sqlite master is a special bulit-in table that lists every table stored inside the database.
# Run this first so you know what data you can explore

tables = pd.read_sql("""SELECT *
    FROM sqlite_master
    WHERE type = 'table';""", conn)
print(tables)

# Read the full Match table and check its shape
matches = pd.read_sql("""SELECT *
    FROM Match;""", conn)
print(matches)
print("Rows and colums:", matches.shape)

# ------ Part 3: SELECT ROws and Columns
# SELECT * fetches every column from a table
# Name specific columns after SELECT to see only those.
# pd.read_sql() runs your SQL and returns a DataFrame/

# Fetch All columns from the Team table
teams = pd.read_sql("""SELECT *
    FROM Team;""", conn)
print(teams)

# Fetch only Team_id and Team_Name columns
team_names = pd.read_sql("""SELECT Team_id, Team_Name
    FROM Team;""", conn)
print(team_names)

# Fetch Match_id and Player_id from Player_Match
player_matches = pd.read_sql("""SELECT Match_id, Player_id
    FROM Player_Match;""", conn)
print(player_matches)

# ------- Part 4: Filter Rows with WHERE ------
# WHERE keeps only the rows that match a condition -
# like a sieve that lets some rows through and blocks others.
# AND combines two conditions (both must be true).
# IN lets you list several allowed values in one go.

# All matches won by  Rajasthan Royals (Team_id = 7)
rr_wins = pd.read_sql("""SELECT *
    FROM Match 
    WHERE Match_Winner == 7;""", conn)
print(rr_wins)

# Mumbai Indians wind only in Season 8 or Season 9
mi_recent = pd.read_sql("""SELECT *
    FROM Match
    WHERE Match_Winner   == 5 AND Season_id IN (8,9);""", conn)
print(mi_recent)


# -------- Part 5: Search for a Pattern with LIKE ------
# LIKE searches for a pattern inside a text column.
# % means zero or more of any charatcer.
# 'De% matches any name that starts with the letter De.
# LIKE always goes inside a WHERE clause.

# Find all teams whose name begins with 'De'
de_teams = pd.read_sql("""SELECT *
    FROM Team
    WHERE Team_Name LIKE 'De%';""", conn)
print(de_teams)

# Find all team whose name ends with 'Kings'
king_teams = pd.read_sql("""SELECT *
    FROM Team
    WHERE Team_Name LIKE '%Kings';""", conn)
print(king_teams)

# ---------- Part 6: Find the Smallest and Largest Values -------------------
# MIN() returns the smallest value in a column
# MAX() returns the largest value in a column
# Write both inside SELECT to compare them in one result

# Find the narrowest and biggest win margins ever recorded
win_margins = pd.read_sql("""SELECT MIN(Win_Margin), SELECT MAX(WIn_Margin)
    FROM Match;""", conn)
print(win_margins)

# Find the earliset and latest Season_id in the database
seasons = pd.read_sql("""SELECT  MIN(Season_id), SELCT MAX(Season_id)
    FROM Match;""", conn)
print(seasons)

conn.close()
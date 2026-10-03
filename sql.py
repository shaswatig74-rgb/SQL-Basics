# print("What is the type of the above given database - \n 1)Relational Database \n 2)Non-Relational Database ")
# answer = int(input("Enter your guess here... "))
# if answer == 2:
#     print("You guessed it right!")
# else:
#     print("Unfortunately your guess was wrong.")

# print("\nPlease tell your mentor why you guessed this?")

import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print("Opened data successfully!")

import pandas as pd
tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type = 'table';",conn)

tables
import sqlite3

# create a connection object
connection = sqlite3.connect("data.db")

# create a cursor using connection object
cursor = connection.cursor()

# cursor object will help us execute sql queries

# query all data based on a condition
cursor.execute("SELECT * FROM events WHERE date='2023.10.15'")
rows = cursor.fetchall()
print(rows)

# query selected columns based on a condition
cursor.execute("SELECT band, date FROM events WHERE date='2023.10.15'")
rows = cursor.fetchall()
print(rows)

# Insert rows
new_rows = [('Cats', 'Cat city', '2023.10.17'), ('Hens', 'Hen city', '2023.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)


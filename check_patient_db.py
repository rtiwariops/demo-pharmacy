import sqlite3

# Create a connection to the database
conn = sqlite3.connect('patients.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Select all rows from the patients table
select_all = 'SELECT * FROM patients'
cursor.execute(select_all)

# Fetch all the rows and print them
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()

import sqlite3

# conn = sqlite3.connect('prescriptions.db')
# cursor = conn.cursor()

# cursor.execute('DROP TABLE prescriptions;')

conn = sqlite3.connect('patients.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE patients;')
cursor.execute('DROP TABLE prescriptions;')

conn.commit()

cursor.close()
conn.close()
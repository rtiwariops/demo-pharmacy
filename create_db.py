import sqlite3

# Create a connection to the database
conn = sqlite3.connect('patients.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create a table named patients with the specified fields
create_table = '''
CREATE TABLE patients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT,
  last_name TEXT,
  guardian TEXT,
  gender TEXT,
  dob TEXT,
  street1 TEXT,
  street2 TEXT,
  city TEXT,
  state TEXT,
  country TEXT,
  zip TEXT,
  phone TEXT,
  email TEXT,
  language_preference TEXT,
  species TEXT,
  viewed_notice_of_privacy_practices INTEGER,
  viewed_notice_of_privacy_practices_date TEXT
);
'''
cursor.execute(create_table)

# Add the data to the table
insert_data = '''
INSERT INTO patients (
  first_name, last_name, guardian, gender, dob, street1, street2, city, state, country, zip,
  phone, email, language_preference, species, viewed_notice_of_privacy_practices, viewed_notice_of_privacy_practices_date
) VALUES (
  'Bruce', 'Banner', 'John', 'male', '19691218', '123 Some Lane', 'Apt. 123', 'Los Angeles', 'CA', 'US', '94402',
  '430-304-3949', 'hulkout@hulk.com', 'English', 'Dog', 1, '20220101'
);
'''
cursor.execute(insert_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

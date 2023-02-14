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

create_table = '''
CREATE TABLE prescriptions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  patient_id INTEGER,
  medication_name TEXT,
  medication_sig TEXT,
  prescriber TEXT,
  date_written TEXT,
  refills_remaining INTEGER,
  current_rx_status_text TEXT,
  fillable INTEGER,
  days_supply TEXT,
  is_refill INTEGER,
  last_filled_date TEXT,
  expiration_date_utc TEXT,
  number_of_refills_allowed INTEGER,
  prescribed_brand_name TEXT,
  prescribed_drug_strength TEXT,
  prescribed_generic_name TEXT,
  prescribed_ndc TEXT,
  prescribed_quantity INTEGER,
  prescribed_written_name TEXT,
  quantity_remaining INTEGER,
  rx_number TEXT,
  origin TEXT,
  prescriber_order_number TEXT,
  original_prescribed_ndc TEXT,
  date_filled_utc TEXT,
  prescribed_quantity_unit TEXT,
  price INTEGER
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

insert_data = '''
INSERT INTO prescriptions (
  patient_id, medication_name, medication_sig, prescriber, date_written, refills_remaining,
  current_rx_status_text, fillable, days_supply, is_refill, last_filled_date,
  expiration_date_utc, number_of_refills_allowed, prescribed_brand_name, prescribed_drug_strength,
  prescribed_generic_name, prescribed_ndc, prescribed_quantity, prescribed_written_name,
  quantity_remaining, rx_number, origin, prescriber_order_number,
  original_prescribed_ndc, date_filled_utc, prescribed_quantity_unit, price
) VALUES (
  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
);
'''
data = (
    1, 'Tafluprost', 'Wake up at midnight, take then.', 'Dr. Bruce Banner', '2020-02-05T00:00:00.000Z', 1,
    'On Hold', 1, '90', 1, '2020-04-08T11:00:00.000Z', '2021-03-31T11:00:00.000Z', 3, 'Zioptan',
    '40 mg', 'Tafluprost 40 mg tablet', '555555555555', 90, 'Tafluprost 40 Mg Tablet', 270, '1144477',
    '5', 'AE1234', 'None', '2020-04-08T11:00:00.000Z', 'EA', 20
)
cursor.execute(insert_data, data)

# Commit the changes and close the connection
conn.commit()
conn.close()

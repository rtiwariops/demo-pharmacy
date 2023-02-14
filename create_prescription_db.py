import sqlite3

# Create a new SQLite database
conn = sqlite3.connect('prescriptions.db')
cursor = conn.cursor()

# Create a new table named prescriptions with a patient_id field
create_table = '''
CREATE TABLE prescriptions (
  id INTEGER PRIMARY KEY,
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
  prescribed_quantity_unit TEXT
);
'''
cursor.execute(create_table)

# Get the patient_id from patientdb
patient_conn = sqlite3.connect('patients.db')
patient_cursor = patient_conn.cursor()

# Assume the patient record with the desired patient_id exists in the patientdb
patient_id = 123

# Insert the data into the prescriptions table with the patient_id value
insert_data = '''
INSERT INTO prescriptions (
  patient_id, medication_name, medication_sig, prescriber, date_written, refills_remaining,
  current_rx_status_text, fillable, days_supply, is_refill, last_filled_date,
  expiration_date_utc, number_of_refills_allowed, prescribed_brand_name, prescribed_drug_strength,
  prescribed_generic_name, prescribed_ndc, prescribed_quantity, prescribed_written_name,
  quantity_remaining, rx_number, origin, prescriber_order_number,
  original_prescribed_ndc, date_filled_utc, prescribed_quantity_unit
) VALUES (
  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
);
'''
data = (
    1, 'Tafluprost', 'Wake up at midnight, take then.', 'Dr. Bruce Banner', '2020-02-05T00:00:00.000Z', 1,
    'On Hold', 1, '90', 1, '2020-04-08T11:00:00.000Z', '2021-03-31T11:00:00.000Z', 3, 'Zioptan',
    '40 mg', 'Tafluprost 40 mg tablet', '555555555555', 90, 'Tafluprost 40 Mg Tablet', 270, '1144477',
    '5', 'AE1234', 'None', '2020-04-08T11:00:00.000Z', 'EA'
)
cursor.execute(insert_data, data)

# Commit the changes and close the connections
conn.commit()
conn.close()
patient_conn.close()

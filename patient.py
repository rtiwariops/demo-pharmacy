from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import uvicorn
app = FastAPI()

# Define a Pydantic model for the patient data
class Patient(BaseModel):
    first_name: str
    last_name: str
    guardian: str
    gender: str
    dob: str
    street1: str
    street2: str
    city: str
    state: str
    country: str
    zip: str
    phone: str
    email: str
    language_preference: str
    species: str
    viewed_notice_of_privacy_practices: bool
    viewed_notice_of_privacy_practices_date: str

@app.get("/patients")
async def get_all_patients():
    # Create a connection to the database
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()

    # Select all rows from the patients table
    select_all = 'SELECT * FROM patients'
    cursor.execute(select_all)

    # Fetch all the rows and convert them to a list of dictionaries
    rows = cursor.fetchall()
    patients = []
    for row in rows:
        patient = {
            'id': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'guardian': row[3],
            'gender': row[4],
            'dob': row[5],
            'street1': row[6],
            'street2': row[7],
            'city': row[8],
            'state': row[9],
            'country': row[10],
            'zip': row[11],
            'phone': row[12],
            'email': row[13],
            'language_preference': row[14],
            'species': row[15],
            'viewed_notice_of_privacy_practices': bool(row[16]),
            'viewed_notice_of_privacy_practices_date': row[17],
        }
        patients.append(patient)

    # Close the connection
    conn.close()

    # Return the list of patients
    return patients

# Define a POST endpoint to add a new patient
@app.post("/patients")
async def add_patient(patient: Patient):
    # Create a connection to the database
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()

    # Insert the patient data into the patients table
    insert_data = '''
    INSERT INTO patients (
      first_name, last_name, guardian, gender, dob, street1, street2, city, state, country, zip,
      phone, email, language_preference, species, viewed_notice_of_privacy_practices, viewed_notice_of_privacy_practices_date
    ) VALUES (
      ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    );
    '''
    cursor.execute(insert_data, (
        patient.first_name, patient.last_name, patient.guardian, patient.gender, patient.dob,
        patient.street1, patient.street2, patient.city, patient.state, patient.country, patient.zip,
        patient.phone, patient.email, patient.language_preference, patient.species,
        int(patient.viewed_notice_of_privacy_practices), patient.viewed_notice_of_privacy_practices_date
    ))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Return the inserted patient data
    return patient

# Define a GET endpoint to retrieve a patient by ID
@app.get("/patients/{patient_id}")
async def get_patient_by_id(patient_id: int):
    # Create a connection to the database
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()

    # Select the row with the specified ID from the patients table
    select_by_id = 'SELECT * FROM patients WHERE id = ?'
    cursor.execute(select_by_id, (patient_id,))

    # Fetch the row and convert it to a dictionary
    row = cursor.fetchone()
    if row is not None:
        patient = {
            'id': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'guardian': row[3],
            'gender': row[4],
            'dob': row[5],
            'street1': row[6],
            'street2': row[7],
            'city': row[8],
            'state': row[9],
            'country': row[10],
            'zip': row[11],
            'phone': row[12],
            'email': row[13],
            'language_preference': row[14],
            'species': row[15],
            'viewed_notice_of_privacy_practices': bool(row[16]),
            'viewed_notice_of_privacy_practices_date': row[17],
        }

        # Close the connection and return the patient data
        conn.close()
        return patient

if __name__ == '__main__':
    uvicorn.run("patient:app", host="0.0.0.0", port=5000, reload=True, workers=2)

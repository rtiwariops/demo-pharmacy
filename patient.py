from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import uvicorn
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# Set up CORS
origins = ["http://localhost", "http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Pydantic model for the patient data
class Patient(BaseModel):
    id: Optional[int]
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
    
class Prescription(BaseModel):
    id: Optional[int]
    patient_id: int = ForeignKey('patient.id', on_delete='CASCADE')
    medication_name: str
    medication_sig: str
    prescriber: str
    date_written: str
    refills_remaining: int
    current_rx_status_text: str
    fillable: bool
    days_supply: str
    is_refill: int
    last_filled_date: str
    expiration_date_utc: str
    number_of_refills_allowed: int
    prescribed_brand_name: str
    prescribed_drug_strength: str
    prescribed_generic_name: str
    prescribed_ndc: str
    prescribed_quantity: int
    prescribed_written_name: str
    quantity_remaining: int
    rx_number: str
    origin: str
    prescriber_order_number: str
    original_prescribed_ndc: str
    date_filled_utc: str
    prescribed_quantity_unit: str

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
        patient = Patient(
            id=row[0],
            first_name=row[1],
            last_name=row[2],
            guardian=row[3],
            gender=row[4],
            dob=row[5],
            street1=row[6],
            street2=row[7],
            city=row[8],
            state=row[9],
            country=row[10],
            zip=row[11],
            phone=row[12],
            email=row[13],
            language_preference=row[14],
            species=row[15],
            viewed_notice_of_privacy_practices=bool(row[16]),
            viewed_notice_of_privacy_practices_date=row[17],
        )
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
    
# Define a PUT endpoint to update an existing patient
@app.put("/patients/{patient_id}")
async def update_patient(patient_id: int, patient: Patient):
    # Create a connection to the database
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()

    # Update the patient data in the patients table
    update_data = '''
    UPDATE patients SET
      first_name = ?,
      last_name = ?,
      guardian = ?,
      gender = ?,
      dob = ?,
      street1 = ?,
      street2 = ?,
      city = ?,
      state = ?,
      country = ?,
      zip = ?,
      phone = ?,
      email = ?,
      language_preference = ?,
      species = ?,
      viewed_notice_of_privacy_practices = ?,
      viewed_notice_of_privacy_practices_date = ?
    WHERE id = ?;
    '''
    cursor.execute(update_data, (
        patient.first_name, patient.last_name, patient.guardian, patient.gender, patient.dob,
        patient.street1, patient.street2, patient.city, patient.state, patient.country, patient.zip,
        patient.phone, patient.email, patient.language_preference, patient.species,
        int(patient.viewed_notice_of_privacy_practices), patient.viewed_notice_of_privacy_practices_date,
        patient_id
    ))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Return the updated patient data
    return patient

@app.get("/prescriptions")
async def get_all_prescriptions():
    # Create a connection to the database
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()

    # Select all rows from the prescriptions table
    select_all = 'SELECT * FROM prescriptions'
    cursor.execute(select_all)

    # Fetch all rows and convert them to dictionaries
    rows = cursor.fetchall()
    prescriptions = []
    for row in rows:
        prescription = {
            'id': row[0],
            'patient_id': row[1],
            'medication_name': row[2],
            'medication_sig': row[3],
            'prescriber': row[4],
            'date_written': row[5],
            'refills_remaining': row[6],
            'current_rx_status_text': row[7],
            'fillable': bool(row[8]),
            'days_supply': row[9],
            'is_refill': row[10],
            'last_filled_date': row[11],
            'expiration_date_utc': row[12],
            'number_of_refills_allowed': row[13],
            'prescribed_brand_name': row[14],
            'prescribed_drug_strength': row[15],
            'prescribed_generic_name': row[16],
            'prescribed_ndc': row[17],
            'prescribed_quantity': row[18],
            'prescribed_written_name': row[19],
            'quantity_remaining': row[20],
            'rx_number': row[21],
            'origin': row[22],
            'prescriber_order_number': row[23],
            'original_prescribed_ndc': row[24],
            'date_filled_utc': row[25],
            'prescribed_quantity_unit': row[26]
        }

        prescriptions.append(Prescription(**prescription))

    # Close the connection and return the prescription data
    conn.close()
    return prescriptions

# Define a GET endpoint to retrieve all prescriptions for a given patient
@app.get("/patients/{patient_id}/prescriptions")
async def get_prescriptions_for_patient(patient_id: int):
    # Create a connection to the patients database
    patients_conn = sqlite3.connect('patients.db')
    patients_cursor = patients_conn.cursor()

    # Select the patient from the patients database
    select_patient = 'SELECT * FROM patients WHERE id = ?'
    patients_cursor.execute(select_patient, (patient_id,))
    patient_row = patients_cursor.fetchone()
    if patient_row is None:
        return None

    # Select all prescriptions for the patient from the prescriptions database
    select_prescriptions = 'SELECT * FROM prescriptions WHERE patient_id = ?'
    patients_cursor.execute(select_prescriptions, (patient_id,))
    prescription_rows = patients_cursor.fetchall()

    # Convert the patient and prescription data to Pydantic models
    patient_data = {
        'id': patient_row[0],
        'first_name': patient_row[1],
        'last_name': patient_row[2],
        'guardian': patient_row[3],
        'gender': patient_row[4],
        'dob': patient_row[5],
        'street1': patient_row[6],
        'street2': patient_row[7],
        'city': patient_row[8],
        'state': patient_row[9],
        'country': patient_row[10],
        'zip': patient_row[11],
        'phone': patient_row[12],
        'email': patient_row[13],
        'language_preference': patient_row[14],
        'species': patient_row[15],
        'viewed_notice_of_privacy_practices': bool(patient_row[16]),
        'viewed_notice_of_privacy_practices_date': patient_row[17],
        'prescriptions': [],
    }
    for prescription_row in prescription_rows:
        prescription_data = {
            'id': prescription_row[0],
            'patient_id': prescription_row[1],
            'medication_name': prescription_row[2],
            'medication_sig': prescription_row[3],
            'prescriber': prescription_row[4],
            'date_written': prescription_row[5],
            'refills_remaining': prescription_row[6],
            'current_rx_status_text': prescription_row[7],
            'fillable': bool(prescription_row[8]),
            'days_supply': prescription_row[9],
            'is_refill': prescription_row[10],
            'last_filled_date': prescription_row[11],
            'expiration_date_utc': prescription_row[12],
            'number_of_refills_allowed': prescription_row[13],
            'prescribed_brand_name': prescription_row[14],
            'prescribed_drug_strength': prescription_row[15],
            'prescribed_generic_name': prescription_row[16],
            'prescribed_ndc': prescription_row[17],
            'prescribed_quantity': prescription_row[18],
            'prescribed_written_name': prescription_row[19],
            'quantity_remaining': prescription_row[20],
            'rx_number': prescription_row[21],
            'origin': prescription_row[22],
            'prescriber_order_number': prescription_row[23],
            'original_prescribed_ndc': prescription_row[24],
            'date_filled_utc': prescription_row[25],
            'prescribed_quantity_unit': prescription_row[26],
        }

        patient_data['prescriptions'].append(prescription_data)

    # Close the database
    patients_conn.close()
    return patient_data
    
# Define a POST endpoint to add a prescription for a given patient
@app.post("/patients/{patient_id}/prescriptions")
async def add_prescription_for_patient(patient_id: int, prescription: dict):
    # Create a connection to the prescriptions database
    with sqlite3.connect('patients.db') as conn:
        c = conn.cursor()
        
        # Select the patient from the patients database
        select_patient = 'SELECT * FROM patients WHERE id = ?'
        c.execute(select_patient, (patient_id,))
        patient_row = c.fetchone()
        print(patient_row)

        # Insert the new prescription into the prescriptions database
        insert_prescription = '''INSERT INTO prescriptions (
                                    patient_id,
                                    medication_name,
                                    medication_sig,
                                    prescriber,
                                    date_written,
                                    refills_remaining,
                                    current_rx_status_text,
                                    fillable,
                                    days_supply,
                                    is_refill,
                                    last_filled_date,
                                    expiration_date_utc,
                                    number_of_refills_allowed,
                                    prescribed_brand_name,
                                    prescribed_drug_strength,
                                    prescribed_generic_name,
                                    prescribed_ndc,
                                    prescribed_quantity,
                                    prescribed_written_name,
                                    quantity_remaining,
                                    rx_number,
                                    origin,
                                    prescriber_order_number,
                                    original_prescribed_ndc,
                                    date_filled_utc,
                                    prescribed_quantity_unit
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        c.execute(insert_prescription, (
            patient_id,
            prescription["medication_name"],
            prescription["medication_sig"],
            prescription["prescriber"],
            prescription["date_written"],
            prescription["refills_remaining"],
            prescription["current_rx_status_text"],
            prescription["fillable"],
            prescription["days_supply"],
            prescription["is_refill"],
            prescription["last_filled_date"],
            prescription["expiration_date_utc"],
            prescription["number_of_refills_allowed"],
            prescription["prescribed_brand_name"],
            prescription["prescribed_drug_strength"],
            prescription["prescribed_generic_name"],
            prescription["prescribed_ndc"],
            prescription["prescribed_quantity"],
            prescription["prescribed_written_name"],
            prescription["quantity_remaining"],
            prescription["rx_number"],
            prescription["origin"],
            prescription["prescriber_order_number"],
            prescription["original_prescribed_ndc"],
            prescription["date_filled_utc"],
            prescription["prescribed_quantity_unit"]
        ))
        conn.commit()

    return {"message": "Prescription added successfully!"}


if __name__ == '__main__':
    uvicorn.run("patient:app", host="0.0.0.0", port=5000, reload=True, workers=2)

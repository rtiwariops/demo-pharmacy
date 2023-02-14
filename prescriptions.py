from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Define a Pydantic model for the prescription data
class Prescription(BaseModel):
    id: int
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

# Define a GET endpoint to retrieve all prescriptions
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
            'medication_name': row[1],
            'medication_sig': row[2],
            'prescriber': row[3],
            'date_written': row[4],
            'refills_remaining': row[5],
            'current_rx_status_text': row[6],
            'fillable': bool(row[7]),
            'days_supply': row[8],
            'is_refill': row[9],
            'last_filled_date': row[10],
            'expiration_date_utc': row[11],
            'number_of_refills_allowed': row[12],
            'prescribed_brand_name': row[13],
            'prescribed_drug_strength': row[14],
            'prescribed_generic_name': row[15],
            'prescribed_ndc': row[16],
            'prescribed_quantity': row[17],
            'prescribed_written_name': row[18],
            'quantity_remaining': row[19],
            'rx_number': row[20],
            'origin': row[21],
            'prescriber_order_number': row[22],
            'original_prescribed_ndc': row[23],
            'date_filled_utc': row[24],
            'prescribed_quantity_unit': row[25],
        }
        prescriptions.append(Prescription(**prescription))

    # Close the connection and return the prescription data
    conn.close()
    return prescriptions

if __name__ == '__main__':
    uvicorn.run("prescriptions:app", host="0.0.0.0", port=5000, reload=True, workers=2)

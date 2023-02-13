from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import SessionLocal
import datetime
from typing import Optional

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    guardian = Column(String)
    gender = Column(String, nullable=False)
    dob = Column(Date, default=datetime.datetime.now, nullable=False)
    street1 = Column(String, nullable=False)
    street2 = Column(String)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    language_preference = Column(String, nullable=False)
    species = Column(String, nullable=False)
    viewed_notice_of_privacy_practices = Column(Boolean, nullable=False)
    viewed_notice_of_privacy_practices_date = Column(Date, default=datetime.datetime.now)

session = SessionLocal()
patient = Patient(first_name="John", last_name="Doe", gender="Male", street1="123 Main St", city="Anytown", state="Anystate", country="Anycountry", zip="12345", phone="555-555-5555", email="john.doe@example.com", language_preference="English", species="Human", viewed_notice_of_privacy_practices=True)
session.add(patient)
session.commit()

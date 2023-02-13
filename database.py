from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

engine = create_engine('sqlite:///patients.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


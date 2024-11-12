import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey

load_dotenv()

DATABASE_URL = f"postgresql://"+\
                f"{os.getenv('DB_USER')}:"+\
                f"{os.getenv('DB_PASSWORD')}@"+\
                f"{os.getenv('DB_HOST')}:"+\
                f"{os.getenv('DB_PORT')}/"+\
                f"{os.getenv('DB_NAME')}"

# Initialize SQLAlchemy Base and engine
Base = declarative_base()
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define ENUM for Providedservices difficulty levels
difficulty_enum = ENUM('легко', 'середнє', 'складно', name='difficulty_enum', create_type=False)


# Models
class Clients(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    telephone = Column(String(50), nullable=False)


class Masters(Base):
    __tablename__ = 'masters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    telephone = Column(String(50), nullable=False)


class Providedservices(Base):
    __tablename__ = 'providedservices'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    category = Column(String(50), nullable=False)
    difficulty = Column(difficulty_enum, nullable=False)


class Repairparts(Base):
    __tablename__ = 'repairparts'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    amount_on_station = Column(Integer, nullable=False)
    amount_on_storage = Column(Integer, nullable=False)


class Responsibles(Base):
    __tablename__ = 'responsibles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    telephone = Column(String(50), nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    manufacture_year = Column(Integer, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)

    client = relationship("Clients")


class Warrantiescards(Base):
    __tablename__ = 'warrantiescards'
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    provided_service_id = Column(Integer, ForeignKey('providedservices.id'), nullable=False)

    vehicle = relationship("Vehicles")
    provided_service = relationship("Providedservices")


class Repairsessions(Base):
    __tablename__ = 'repairsessions'
    id = Column(Integer, primary_key=True)
    order_number = Column(String(50), nullable=False)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=True)
    malfunctions = Column(String(255), nullable=True)
    order_comment = Column(String(255), nullable=True)
    total_sum = Column(Integer, nullable=False)
    paid_sum = Column(Integer, nullable=False)
    if_finished = Column(Boolean, nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    responsible_id = Column(Integer, ForeignKey('responsibles.id'), nullable=False)
    master_id = Column(Integer, ForeignKey('masters.id'), nullable=False)

    vehicle = relationship("Vehicles")
    responsible = relationship("Responsibles")
    master = relationship("Masters")
    repair_parts = relationship("Repairparts", secondary="repairsessions_repairparts")
    provided_services = relationship("Providedservices", secondary="repairsessions_providedservices")


class RepairsessionsRepairparts(Base):
    __tablename__ = 'repairsessions_repairparts'
    repair_session_id = Column(Integer, ForeignKey('repairsessions.id'), primary_key=True)
    repair_part_id = Column(Integer, ForeignKey('repairparts.id'), primary_key=True)
    amount = Column(Integer, default=0)


class RepairsessionsProvidedservices(Base):
    __tablename__ = 'repairsessions_providedservices'
    repair_session_id = Column(Integer, ForeignKey('repairsessions.id'), primary_key=True)
    provided_service_id = Column(Integer, ForeignKey('providedservices.id'), primary_key=True)

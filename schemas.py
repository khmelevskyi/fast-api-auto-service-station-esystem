from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# --- Pydantic Models for each Django Model ---


# Pydantic model for Clients
class Client(BaseModel):
    id: int
    name: str = Field(..., max_length=50)
    telephone: str = Field(..., max_length=50)

    class Config:
        from_attributes = True

class ClientCreate(BaseModel):
    name: str = Field(..., max_length=50)
    telephone: str = Field(..., max_length=50)


# Pydantic model for Masters
class Master(BaseModel):
    id: int
    name: str = Field(..., max_length=50)
    telephone: str = Field(..., max_length=50)

    class Config:
        from_attributes = True

class MasterCreate(BaseModel):
    name: str = Field(..., max_length=50)
    telephone: str = Field(..., max_length=50)


# Pydantic model for Providedservices
class ProvidedService(BaseModel):
    id: int
    name: str = Field(..., max_length=50)
    category: str = Field(..., max_length=50)
    difficulty: str

    class Config:
        from_attributes = True

class ProvidedServiceCreate(BaseModel):
    name: str = Field(..., max_length=50)
    category: str = Field(..., max_length=50)
    difficulty: str


# Pydantic model for Repairparts
class RepairPart(BaseModel):
    id: int
    name: str = Field(..., max_length=50)
    amount_on_station: int
    amount_on_storage: int

    class Config:
        from_attributes = True

class RepairPartCreate(BaseModel):
    name: str = Field(..., max_length=50)
    amount_on_station: int
    amount_on_storage: int


# Pydantic model for Responsibles
class Responsible(BaseModel):
    id: int
    name: str = Field(..., max_length=50)
    telephone: str = Field(..., max_length=50)

    class Config:
        from_attributes = True

class ResponsibleCreate(BaseModel):
    name: str = Field(..., max_length=50)
    telephone: str = Field(..., max_length=50)


# Pydantic model for Vehicles
class Vehicle(BaseModel):
    id: int
    brand: str = Field(..., max_length=50)
    model: str = Field(..., max_length=50)
    manufacture_year: int
    client_id: int  # ForeignKey relationship to Client

    class Config:
        from_attributes = True

class VehicleCreate(BaseModel):
    brand: str = Field(..., max_length=50)
    model: str = Field(..., max_length=50)
    manufacture_year: int
    client_id: int  # ForeignKey relationship to Client


# Pydantic model for Warrantiescards
class WarrantyCard(BaseModel):
    id: int
    start_date: datetime
    end_date: datetime
    vehicle_id: int  # ForeignKey relationship to Vehicle
    provided_service_id: int  # ForeignKey relationship to ProvidedService

    class Config:
        from_attributes = True

class WarrantyCardCreate(BaseModel):
    start_date: datetime
    end_date: datetime
    vehicle_id: int  # ForeignKey relationship to Vehicle
    provided_service_id: int  # ForeignKey relationship to ProvidedService


# Pydantic model for Repairsessions
class RepairSession(BaseModel):
    id: int
    order_number: str = Field(..., max_length=50)
    date_start: datetime
    date_end: datetime
    malfunctions: Optional[str] = Field(None, max_length=255)
    order_comment: Optional[str] = Field(None, max_length=255)
    total_sum: int
    paid_sum: int
    if_finished: bool
    vehicle_id: int  # ForeignKey relationship to Vehicle
    responsible_id: int  # ForeignKey relationship to Responsible
    master_id: int  # ForeignKey relationship to Master

    class Config:
        from_attributes = True

class RepairSessionCreate(BaseModel):
    order_number: str = Field(..., max_length=50)
    date_start: datetime
    date_end: datetime
    malfunctions: Optional[str] = Field(None, max_length=255)
    order_comment: Optional[str] = Field(None, max_length=255)
    total_sum: int
    paid_sum: int
    if_finished: bool
    vehicle_id: int  # ForeignKey relationship to Vehicle
    responsible_id: int  # ForeignKey relationship to Responsible
    master_id: int  # ForeignKey relationship to Master


# Pydantic model for RepairsessionsProvidedservices
class RepairSessionProvidedService(BaseModel):
    repair_session_id: int  # ForeignKey to RepairSession
    provided_service_id: int  # ForeignKey to ProvidedService

    class Config:
        from_attributes = True


# Pydantic model for RepairsessionsRepairparts
class RepairSessionRepairPart(BaseModel):
    repair_session_id: int  # ForeignKey to RepairSession
    repair_part_id: int  # ForeignKey to RepairPart
    amount: int

    class Config:
        from_attributes = True

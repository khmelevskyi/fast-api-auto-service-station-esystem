from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func
from typing import List
from models import (
    SessionLocal,
    Clients, Masters, Providedservices,
    Repairparts, Responsibles, Vehicles,
    Warrantiescards, Repairsessions
)
from schemas import (
    Client, ClientCreate,
    Master, MasterCreate,
    ProvidedService, ProvidedServiceCreate,
    RepairPart, RepairPartCreate,
    Responsible, ResponsibleCreate,
    Vehicle, VehicleCreate,
    WarrantyCard, WarrantyCardCreate,
    RepairSession, RepairSessionCreate
)

# Initialize FastAPI
app = FastAPI()

# Dependency to get DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- CRUD Endpoints for Clients ---
@app.get("/clients/", response_model=List[Client])
def get_all_clients(db: Session = Depends(get_db)):
    return db.query(Clients).all()

@app.get("/clients/{client_id}", response_model=Client)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Clients).filter(Clients.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@app.post("/clients/", response_model=Client)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    # Retrieve the latest client ID and add 1
    latest_client_id = db.query(func.max(Clients.id)).scalar() or 0
    new_client = Clients(id=latest_client_id + 1, **client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

@app.put("/clients/{client_id}", response_model=Client)
def update_client(client_id: int, client: Client, db: Session = Depends(get_db)):
    db_client = db.query(Clients).filter(Clients.id == client_id).first()
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    for key, value in client.dict().items():
        setattr(db_client, key, value)
    db.commit()
    db.refresh(db_client)
    return db_client

@app.delete("/clients/{client_id}", response_model=dict)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    db_client = db.query(Clients).filter(Clients.id == client_id).first()
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(db_client)
    db.commit()
    return {"message": "Client deleted successfully"}


# --- CRUD Endpoints for Masters ---
@app.get("/masters/", response_model=List[Master])
def get_all_masters(db: Session = Depends(get_db)):
    return db.query(Masters).all()

@app.get("/masters/{master_id}", response_model=Master)
def get_master(master_id: int, db: Session = Depends(get_db)):
    master = db.query(Masters).filter(Masters.id == master_id).first()
    if master is None:
        raise HTTPException(status_code=404, detail="Master not found")
    return master

@app.post("/masters/", response_model=Master)
def create_master(master: MasterCreate, db: Session = Depends(get_db)):
    # Retrieve the latest master ID and add 1
    latest_master_id = db.query(func.max(Masters.id)).scalar() or 0
    new_master = Masters(id=latest_master_id + 1, **master.dict())
    db.add(new_master)
    db.commit()
    db.refresh(new_master)
    return new_master

@app.put("/masters/{master_id}", response_model=Master)
def update_master(master_id: int, master: Master, db: Session = Depends(get_db)):
    db_master = db.query(Masters).filter(Masters.id == master_id).first()
    if db_master is None:
        raise HTTPException(status_code=404, detail="Master not found")
    for key, value in master.dict().items():
        setattr(db_master, key, value)
    db.commit()
    db.refresh(db_master)
    return db_master

@app.delete("/masters/{master_id}", response_model=dict)
def delete_master(master_id: int, db: Session = Depends(get_db)):
    db_master = db.query(Masters).filter(Masters.id == master_id).first()
    if db_master is None:
        raise HTTPException(status_code=404, detail="Master not found")
    db.delete(db_master)
    db.commit()
    return {"message": "Master deleted successfully"}


# --- CRUD Endpoints for Provided Services ---
@app.get("/providedservices/", response_model=List[ProvidedService])
def get_all_providedservices(db: Session = Depends(get_db)):
    return db.query(Providedservices).all()

@app.get("/providedservices/{service_id}", response_model=ProvidedService)
def get_providedservice(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Providedservices).filter(Providedservices.id == service_id).first()
    if service is None:
        raise HTTPException(status_code=404, detail="Provided Service not found")
    return service

@app.post("/providedservices/", response_model=ProvidedService)
def create_providedservice(service: ProvidedServiceCreate, db: Session = Depends(get_db)):
    # Retrieve the latest providedservice ID and add 1
    latest_service_id = db.query(func.max(Providedservices.id)).scalar() or 0
    new_service = Providedservices(id=latest_service_id + 1, **service.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

@app.put("/providedservices/{service_id}", response_model=ProvidedService)
def update_providedservice(service_id: int, service: ProvidedService, db: Session = Depends(get_db)):
    db_service = db.query(Providedservices).filter(Providedservices.id == service_id).first()
    if db_service is None:
        raise HTTPException(status_code=404, detail="Provided Service not found")
    for key, value in service.dict().items():
        setattr(db_service, key, value)
    db.commit()
    db.refresh(db_service)
    return db_service

@app.delete("/providedservices/{service_id}", response_model=dict)
def delete_providedservice(service_id: int, db: Session = Depends(get_db)):
    db_service = db.query(Providedservices).filter(Providedservices.id == service_id).first()
    if db_service is None:
        raise HTTPException(status_code=404, detail="Provided Service not found")
    db.delete(db_service)
    db.commit()
    return {"message": "Provided Service deleted successfully"}

# --- Repairparts CRUD Endpoints ---
@app.get("/repairparts/", response_model=list[RepairPart])
def get_all_repairparts(db: Session = Depends(get_db)):
    return db.query(Repairparts).all()

@app.get("/repairparts/{id}", response_model=RepairPart)
def get_repairpart_by_id(id: int, db: Session = Depends(get_db)):
    repairpart = db.query(Repairparts).filter(Repairparts.id == id).first()
    if not repairpart:
        raise HTTPException(status_code=404, detail="Repair part not found")
    return repairpart

@app.put("/repairparts/{id}", response_model=RepairPart)
def update_repairpart(id: int, repairpart: RepairPartCreate, db: Session = Depends(get_db)):
    db_repairpart = db.query(Repairparts).filter(Repairparts.id == id).first()
    if not db_repairpart:
        raise HTTPException(status_code=404, detail="Repair part not found")
    for key, value in repairpart.dict().items():
        setattr(db_repairpart, key, value)
    db.commit()
    db.refresh(db_repairpart)
    return db_repairpart

@app.delete("/repairparts/{id}", response_model=dict)
def delete_repairpart(id: int, db: Session = Depends(get_db)):
    db_repairpart = db.query(Repairparts).filter(Repairparts.id == id).first()
    if not db_repairpart:
        raise HTTPException(status_code=404, detail="Repair part not found")
    db.delete(db_repairpart)
    db.commit()
    return {"detail": "Repair part deleted"}

@app.post("/repairparts/", response_model=RepairPart)
def create_repairpart(repairpart: RepairPartCreate, db: Session = Depends(get_db)):
    latest_id = db.query(func.max(Repairparts.id)).scalar() or 0
    new_repairpart = Repairparts(id=latest_id + 1, **repairpart.dict())
    db.add(new_repairpart)
    db.commit()
    db.refresh(new_repairpart)
    return new_repairpart

# --- Responsibles CRUD Endpoints ---
@app.get("/responsibles/", response_model=list[Responsible])
def get_all_responsibles(db: Session = Depends(get_db)):
    return db.query(Responsibles).all()

@app.get("/responsibles/{id}", response_model=Responsible)
def get_responsible_by_id(id: int, db: Session = Depends(get_db)):
    responsible = db.query(Responsibles).filter(Responsibles.id == id).first()
    if not responsible:
        raise HTTPException(status_code=404, detail="Responsible not found")
    return responsible

@app.put("/responsibles/{id}", response_model=Responsible)
def update_responsible(id: int, responsible: ResponsibleCreate, db: Session = Depends(get_db)):
    db_responsible = db.query(Responsibles).filter(Responsibles.id == id).first()
    if not db_responsible:
        raise HTTPException(status_code=404, detail="Responsible not found")
    for key, value in responsible.dict().items():
        setattr(db_responsible, key, value)
    db.commit()
    db.refresh(db_responsible)
    return db_responsible

@app.delete("/responsibles/{id}", response_model=dict)
def delete_responsible(id: int, db: Session = Depends(get_db)):
    db_responsible = db.query(Responsibles).filter(Responsibles.id == id).first()
    if not db_responsible:
        raise HTTPException(status_code=404, detail="Responsible not found")
    db.delete(db_responsible)
    db.commit()
    return {"detail": "Responsible deleted"}

@app.post("/responsibles/", response_model=Responsible)
def create_responsible(responsible: ResponsibleCreate, db: Session = Depends(get_db)):
    latest_id = db.query(func.max(Responsibles.id)).scalar() or 0
    new_responsible = Responsibles(id=latest_id + 1, **responsible.dict())
    db.add(new_responsible)
    db.commit()
    db.refresh(new_responsible)
    return new_responsible

# --- Vehicles CRUD Endpoints ---
@app.get("/vehicles/", response_model=list[Vehicle])
def get_all_vehicles(db: Session = Depends(get_db)):
    return db.query(Vehicles).all()

@app.get("/vehicles/{id}", response_model=Vehicle)
def get_vehicle_by_id(id: int, db: Session = Depends(get_db)):
    vehicle = db.query(Vehicles).filter(Vehicles.id == id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@app.put("/vehicles/{id}", response_model=Vehicle)
def update_vehicle(id: int, vehicle: VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = db.query(Vehicles).filter(Vehicles.id == id).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    for key, value in vehicle.dict().items():
        setattr(db_vehicle, key, value)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

@app.delete("/vehicles/{id}", response_model=dict)
def delete_vehicle(id: int, db: Session = Depends(get_db)):
    db_vehicle = db.query(Vehicles).filter(Vehicles.id == id).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    db.delete(db_vehicle)
    db.commit()
    return {"detail": "Vehicle deleted"}

@app.post("/vehicles/", response_model=Vehicle)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    latest_id = db.query(func.max(Vehicles.id)).scalar() or 0
    new_vehicle = Vehicles(id=latest_id + 1, **vehicle.dict())
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle

# --- Warrantiescards CRUD Endpoints ---
@app.get("/warrantiescards/", response_model=list[WarrantyCard])
def get_all_warrantiescards(db: Session = Depends(get_db)):
    return db.query(Warrantiescards).all()

@app.get("/warrantiescards/{id}", response_model=WarrantyCard)
def get_warrantiescard_by_id(id: int, db: Session = Depends(get_db)):
    warranty = db.query(Warrantiescards).filter(Warrantiescards.id == id).first()
    if not warranty:
        raise HTTPException(status_code=404, detail="Warranty card not found")
    return warranty

@app.put("/warrantiescards/{id}", response_model=WarrantyCard)
def update_warrantiescard(id: int, warranty: WarrantyCardCreate, db: Session = Depends(get_db)):
    db_warranty = db.query(Warrantiescards).filter(Warrantiescards.id == id).first()
    if not db_warranty:
        raise HTTPException(status_code=404, detail="Warranty card not found")
    for key, value in warranty.dict().items():
        setattr(db_warranty, key, value)
    db.commit()
    db.refresh(db_warranty)
    return db_warranty

@app.delete("/warrantiescards/{id}", response_model=dict)
def delete_warrantiescard(id: int, db: Session = Depends(get_db)):
    db_warranty = db.query(Warrantiescards).filter(Warrantiescards.id == id).first()
    if not db_warranty:
        raise HTTPException(status_code=404, detail="Warranty card not found")
    db.delete(db_warranty)
    db.commit()
    return {"detail": "Warranty card deleted"}

@app.post("/warrantiescards/", response_model=WarrantyCard)
def create_warrantiescard(warranty: WarrantyCardCreate, db: Session = Depends(get_db)):
    latest_id = db.query(func.max(Warrantiescards.id)).scalar() or 0
    new_warranty = Warrantiescards(id=latest_id + 1, **warranty.dict())
    db.add(new_warranty)
    db.commit()
    db.refresh(new_warranty)
    return new_warranty

# --- Repairsessions CRUD Endpoints ---
@app.get("/repairsessions/", response_model=list[RepairSession])
def get_all_repairsessions(db: Session = Depends(get_db)):
    return db.query(Repairsessions).all()

@app.get("/repairsessions/{id}", response_model=RepairSession)
def get_repairsession_by_id(id: int, db: Session = Depends(get_db)):
    session = db.query(Repairsessions).filter(Repairsessions.id == id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Repair session not found")
    return session

@app.put("/repairsessions/{id}", response_model=RepairSession)
def update_repairsession(id: int, session: RepairSessionCreate, db: Session = Depends(get_db)):
    db_session = db.query(Repairsessions).filter(Repairsessions.id == id).first()
    if not db_session:
        raise HTTPException(status_code=404, detail="Repair session not found")
    for key, value in session.dict().items():
        setattr(db_session, key, value)
    db.commit()
    db.refresh(db_session)
    return db_session

@app.delete("/repairsessions/{id}", response_model=dict)
def delete_repairsession(id: int, db: Session = Depends(get_db)):
    db_session = db.query(Repairsessions).filter(Repairsessions.id == id).first()
    if not db_session:
        raise HTTPException(status_code=404, detail="Repair session not found")
    db.delete(db_session)
    db.commit()
    return {"detail": "Repair session deleted"}

@app.post("/repairsessions/", response_model=RepairSession)
def create_repairsession(session: RepairSessionCreate, db: Session = Depends(get_db)):
    latest_id = db.query(func.max(Repairsessions.id)).scalar() or 0
    new_session = Repairsessions(id=latest_id + 1, **session.dict())
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session
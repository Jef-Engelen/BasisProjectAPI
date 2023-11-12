from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

app = FastAPI()

# CORS inschakelen
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQL database opzetten
DATABASE_URL = "sqlite:///groceries.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modellen aanmaken voor db
class Grocery(Base):
    __tablename__ = "groceries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    brand = Column(String)

# Aanmaken tabellen
Base.metadata.create_all(bind=engine)

# Klasse voor het aanmaken van een payload
class GroceryCreate(BaseModel):
    name: str
    brand: str = None

# API routes
@app.get("/api/groceries")
def get_groceries():
    with SessionLocal() as db:
        groceries = db.query(Grocery).all()
        return {"groceries": [{"id": grocery.id, "name": grocery.name, "brand": grocery.brand} for grocery in groceries]}

@app.post("/api/groceries")
def create_grocery(grocery: GroceryCreate):
    with SessionLocal() as db:
        new_grocery = Grocery(**grocery.dict())
        db.add(new_grocery)
        db.commit()
        db.refresh(new_grocery)
        return {"grocery": {"id": new_grocery.id, "name": new_grocery.name, "brand": new_grocery.brand}}, 201

@app.get("/api/groceries/{grocery_id}")
def get_grocery(grocery_id: int):
    with SessionLocal() as db:
        grocery = db.query(Grocery).filter(Grocery.id == grocery_id).first()
        if grocery:
            return {"grocery": {"id": grocery.id, "name": grocery.name, "brand": grocery.brand}}
        else:
            raise HTTPException(status_code=404, detail="Grocery not found")

@app.delete("/api/groceries/{grocery_id}")
def delete_grocery(grocery_id: int):
    with SessionLocal() as db:
        grocery = db.query(Grocery).filter(Grocery.id == grocery_id).first()
        if grocery:
            db.delete(grocery)
            db.commit()
            return {"message": "Grocery deleted"}
        else:
            raise HTTPException(status_code=404, detail="Grocery not found")

@app.put("/api/groceries/{grocery_id}")
def update_grocery(grocery_id: int, grocery_update: GroceryCreate = Body(...)):
    with SessionLocal() as db:
        grocery = db.query(Grocery).filter(Grocery.id == grocery_id).first()
        if grocery:
            grocery.name = grocery_update.name
            grocery.brand = grocery_update.brand
            db.commit()
            return {"grocery": {"id": grocery.id, "name": grocery.name, "brand": grocery.brand}}
        else:
            raise HTTPException(status_code=404, detail="Grocery not found")

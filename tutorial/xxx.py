from typing import List
from fastapi import APIRouter, Depends
from fastsql import CRUD, schemas
app01 = APIRouter()

@app01.get("/getnumber/{number}", response_model=schemas.ReadUser)


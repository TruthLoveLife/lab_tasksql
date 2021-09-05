from pydantic import BaseModel


class ReadUser(BaseModel):
    personal_id: int
    name: str
    sex: str
    birthdate: int


class CreatUser(BaseModel):
    name: str
    sex: str

class Result_Model(BaseModel):
    number: int

class InPerson_Mosel(BaseModel):
    personid: str
    name: str
    sex: str
    minzu: str
    birthday: str
    huzhu: str
    age: str


class CreateOrder(BaseModel):
    name:str
    table: str
    stool: str
    bed: str
    cabinet: str
    computer_table: str
    phone: str


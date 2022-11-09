#Librerias

#Python


#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI

#Modelo
class Item(BaseModel): #item extiende de basemodel
    name: str
    description: str | None = None #Atributos ops
    price: float
    tax: float | None = None

#Instancia
app = FastAPI()

#Methodos get

#Ruta root
@app.get("/")
async def root():
    return {"message": "Hello World"}

#Path parametros --> obligatorios
@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id}

#Base de datos simulada
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#Query parametros --> ops
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]



#Metodo Post

@app.post("/items/")
async def create_item(item: Item):
    return item
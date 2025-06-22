
"""
GET /
Returns a welcome message.
Returns:
    dict: A dictionary containing a greeting message.
"""
...
"""
GET /saludo/{nombre}
Returns a greeting and a calculation result for the given name.
Args:
    nombre (str): The name to include in the greeting.
Returns:
    dict: A dictionary with a greeting, calculation result, and the name.
"""
...
"""
GET /person/{id}
Retrieves a person by their ID from the data file.
Args:
    id (int): The ID of the person to retrieve.
Returns:
    Person | dict: The Person object if found, otherwise an error message.
"""
...
"""
Loads a list of Person objects from a JSON file.
Args:
    file_path (str): The path to the JSON file containing people data.
Returns:
    list[Person]: A list of Person objects loaded from the file.
"""
...
# from app.personDTO import Person
from app.domain.entities.personBE import Person,Address
from app.domain.entities.personDTO import PersonDTO, AddressDTO
from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

app.title= "Olecram API"
app.version= "1.0.3"

@app.get("/",tags=("home"))
def home():
    return {"mensaje": "Hola Marcelo desde FastAPI + .venv!"}

@app.get("/saludo/{nombre}",tags=("home"))
def saludo(nombre: str):
    x = 1.54
    y= 20
    res =  y/y
    resToObject = {
     "saludo" : "Hola bebe",
     "calculo" : res,
     "name":f"Hola  { nombre}"
    }


    return resToObject

 
@app.get("/person/{id}",tags=("persons"))
def getPerson(id: int):


    persons= load_people_from_file("data.json")

    if persons is None:
     return {"error": "Person not found by errors"}

    # Find the person with the given id
    person_obj = next((p for p in persons if p.id == id), None)

    
    if person_obj is None:
       return {"error": "Person not found"}
    
    person =person_obj
    
    return person
    


#---------------------------------------other functions--------------------------------

def load_people_from_file(file_name: str) -> list[Person]:
    try:
        base_dir = os.path.dirname(__file__)  # ruta donde está este script
        file_path = os.path.join(base_dir, file_name)

        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        
        people = [Person(**item) for item in raw_data]
        # people = Person.model_validate_json(raw_data,many= True)
        return people

    # except FileNotFoundError:
    #     print(f"❌ Archivo no encontrado: {file_path}")
        
    # except json.JSONDecodeError:
    #     print("❌ Error al parsear el JSON (formato inválido)")
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None        


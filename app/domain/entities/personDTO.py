from typing import List, Optional
from pydantic import BaseModel, Field

from app.domain.entities.personBE import Address, Person

class AddressDTO(BaseModel):
    street: str
    city: str
    zip_code: str
    state:str
    type:str
    def __repr__(self):
        return f"Address(street='{self.street}', city='{self.city}', zip_code='{self.zip_code}')"

class PersonDTO(BaseModel):
    id: int 
    first_name: str
    last_name: str
    age: int
    addresses: List[AddressDTO] = []
    # addresses: Optional[Address] = None  # opcional si puede faltar
    
    # consola  print   for print(p)  
    # usado por print(), logs, repr(), y el shell de Python.
    def __repr__(self):
        return (f"Person(first_name='{self.first_name}', last_name='{self.last_name}', "
                f"age={self.age}, addresses={self.addresses})")
    
    #  usado por print() cuando ambos existen
    def __str__(self):
        return f"{self.name} ({self.age} años)"




def dto_to_entity(dto: PersonDTO) -> Person:
        """
        Converts a PersonDTO object to a Person entity.

        Args:
            dto (PersonDTO): The data transfer object containing person information.

        Returns:
            Person: The corresponding Person entity with all fields mapped, including a list of Address entities.

        Note:
            Assumes that dto.addresses is a list of AddressDTO objects, each of which can be converted to an Address entity using their dict representation.
        """
        addresses = [Address(**a.model_dump()) for a in dto.addresses]
        return Person(
            id=dto.id,
            first_name=dto.first_name,
            last_name=dto.last_name,
            age=dto.age,
            addresses=addresses
        )

# entity_to_dto: Convert a Person entity to a PersonDTO.
def entity_to_dto(entity: Person) -> PersonDTO:
    """Converts a Person entity to a PersonDTO object.
    Args:
        entity (Person): The Person entity to convert.  
    """
    addresses = [AddressDTO(**vars(a)) for a in entity.addresses]
    return PersonDTO(
        id=entity.id,
        first_name=entity.first_name,
        last_name=entity.last_name,
        age=entity.age,
        addresses=addresses
    )
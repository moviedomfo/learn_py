from dataclasses import dataclass
from typing import List

@dataclass
class Address:
    type: str
    street: str
    city: str
    province: str
    zip_code: str

@dataclass
class Person:
    id: int
    first_name: str
    last_name: str
    age: int
    addresses: List[Address]

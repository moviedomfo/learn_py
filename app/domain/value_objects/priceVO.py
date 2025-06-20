from dataclasses import dataclass
from enum import StrEnum

class CurrencyOption(StrEnum):
    euro = "EUR"
    dolar ="U$S"
    ar ="ARG"

@dataclass
class Price:
    value: float
    currency: CurrencyOption
from datetime import date
from pydantic import BaseModel


class RateQueryParams(BaseModel):
    date_from: date
    date_to: date
    origin: str
    destination: str

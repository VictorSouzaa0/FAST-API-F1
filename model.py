from typing import  Optional
from pydantic import BaseModel

class CurrentSeason(BaseModel):
    id: Optional[int] = None
    name: str
    team: str
    country: str
    podiums: int
    wdc: int
    wins: int

class HallFame(BaseModel):
    id: Optional[int] = None
    team: str
    country: str
    podiums: int
    wdc: int
    wins: int
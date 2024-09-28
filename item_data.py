from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: str
    student: Optional[bool]
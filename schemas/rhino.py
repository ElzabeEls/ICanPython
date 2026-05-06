from pydantic import BaseModel, Field


class RhinoSchema(BaseModel):
    name: str
    age: int = Field(ge=1)  # ge means "greater than or equal to"
    is_alive: bool = True

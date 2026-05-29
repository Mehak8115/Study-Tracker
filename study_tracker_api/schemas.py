from pydantic import BaseModel, Field

class SessionCreate(BaseModel):
    topic: str
    hours_spent: float = Field(gt=0)
    status: str

class SessionResponse(SessionCreate):
    id: int

    class Config:
        from_attributes = True
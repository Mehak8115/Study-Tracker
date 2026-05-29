from pydantic import BaseModel

class SessionCreate(BaseModel):
    topic: str
    hours_spent: float
    status: str


class SessionResponse(SessionCreate):
    id: int

    class Config:
        from_attributes = True
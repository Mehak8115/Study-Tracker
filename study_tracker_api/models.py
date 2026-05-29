from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

created_at = Column(
    DateTime,
    default=datetime.utcnow
)

class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, index=True)
    hours_spent = Column(Float)
    status = Column(String)
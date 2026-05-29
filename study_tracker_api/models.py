from sqlalchemy import Column, Integer, String, Float
from database import Base

class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, index=True)
    hours_spent = Column(Float)
    status = Column(String)
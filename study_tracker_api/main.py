# stores all the data but if server restarts everything is lost,hence using SQLlite 
# sessions = []

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Study Tracker"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/sessions")
def create_session(
    session: schemas.SessionCreate, #input from user
    db: Session = Depends(get_db) 
):
    new_session = models.StudySession(
        topic=session.topic,
        hours_spent=session.hours_spent,
        status=session.status
    )

    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    return new_session

@app.get("/sessions")
def get_sessions(
    db: Session = Depends(get_db)
):
    return db.query(
        models.StudySession
    ).all()

@app.get("/sessions/{session_id}")
def get_sessions_id(
    session_id:int,
    db: Session = Depends(get_db)
):
    session= db.query(models.StudySession)\
               .filter(models.StudySession.id == session_id)\
               .first()
    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )
    return session


@app.put("/sessions/{session_id}")
def update_session(
    session_id: int, #input from user
    updated_data: schemas.SessionCreate, #input from user
    db: Session = Depends(get_db)
):
    session = db.query(models.StudySession)\
                .filter(models.StudySession.id == session_id)\
                .first()

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    session.topic = updated_data.topic
    session.hours_spent = updated_data.hours_spent
    session.status = updated_data.status

    db.commit()
    db.refresh(session)

    return session

@app.delete("/sessions/{session_id}")
def delete_session(
    session_id: int, #input from user
    db: Session = Depends(get_db)
):
    session = db.query(models.StudySession)\
                .filter(models.StudySession.id == session_id)\
                .first()

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )
    db.delete(session)
    db.commit()
    
    return {"message":"Session deleted successfully"}
from app.db.connection import Session

def get_session_db():
    try:
        session = Session()
        yield session
    finally:
        session.close()
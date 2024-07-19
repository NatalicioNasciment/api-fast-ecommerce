from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.schemes.category import Category
from app.routers.deps import get_session_db
from app.use_cases.category import CategoryUseCases 

router = APIRouter(prefix='/category', tags=["Category"])

@router.post("/add")
def add_category(
    category: Category,
    db_session: Session = Depends(get_session_db)
):
    uc = CategoryUseCases(db_session=db_session)

    uc.add_category(category=category)
    
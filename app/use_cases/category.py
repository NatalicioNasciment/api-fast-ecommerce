from sqlalchemy.orm import Session
from app.schemes.category import Category
from app.db.models import Category as CategoryModel

class CategoryUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def add_category(self, category: Category):
        category_model = CategoryModel(**category.model_dump())
        self.db_session.add(category_model)
        self.db_session.commit()
from app.use_cases.category import CategoryUseCases
from app.db.models import Category as CategoryModel
from app.schemes.category import Category

def test_add_category_use_case(db_session):
    category_use_case = CategoryUseCases(db_session)
    
    category = Category(
        name='Roupa',
        slug='roupa'
    )

    category_use_case.add_category(category=category)

    categories_on_db = db_session.query(CategoryModel).all()

    assert len(categories_on_db) == 1
    assert categories_on_db[0].name == category.name
    assert categories_on_db[0].slug == category.slug

    db_session.delete(categories_on_db[0])
    db_session.commit()
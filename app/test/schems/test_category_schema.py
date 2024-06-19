import pytest
from app.schemes.category import Category

def test_category_schema():
    category = Category(
        name='Roupa',
        slug='roupa'
    )

    assert category.model_dump() == {
       'name': 'Roupa',
       'slug': 'roupa' 
    }

def test_category_schema_invalid_slug():

    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='roupa de cama'
        )
        
    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='ç&ã'
        )
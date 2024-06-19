from app.schemes.base import CustomBaseModel
from pydantic import field_validator
import re

class Category(CustomBaseModel):
    name: str
    slug: str

    @field_validator('slug')
    def field_validator_slug(cls, value):

        if not re.match('^[a-z0-9]+(?:-[a-z0-9]+)*$', value):
            raise ValueError('Invalid slug')
        
        return value

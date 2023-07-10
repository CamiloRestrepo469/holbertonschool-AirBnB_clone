#!/usr/bin/python3
import uuid
from datetime import datetime
"""create a new class BaseModel"""

class BaseModel:
    """Base class for all models"""
    def __init__(self):
        """Create a constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    """create update methods"""
    def update(self):
        self.updated_at = datetime.now()
        
    def save(self):
        self.update()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def to_dict(self):
        attributes = {key: value for key, value in self.__dict__.items() if not key.startswith('__')}
        attributes['__class__'] = self.__class__.__name__
        attributes['created_at'] = self.created_at.isoformat()
        attributes['updated_at'] = self.updated_at.isoformat()
        return attributes
        
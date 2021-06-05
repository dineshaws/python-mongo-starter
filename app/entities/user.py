from pydantic import BaseModel
from typing import Optional

'''
Class to validate router payload
'''
class User(BaseModel):
    email: str
    name: str
    password: str

from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4

class Gender(str, Enum):
  male = 'male'
  female = 'female'

class Role(str, Enum):
  admin = 'admin'
  user = 'user'
  student = 'student'
   
class User(BaseModel):
  id: Optional[UUID] = Field(default_factory=uuid4)
  first_name: str
  last_name: str
  middle_name: Optional[str]
  gender: Gender
  roles: List[Role]

class UserUpdateRequest(BaseModel):
  first_name: Optional[str]
  last_name: Optional[str]
  middle_name: Optional[str]
  gender: Optional[Gender]
  roles: Optional[List[Role]]



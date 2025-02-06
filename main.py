from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(id=UUID("f47ac10b-58cc-4372-a567-0e02b2c3d479"), first_name="John", last_name="Doe", middle_name="Doe", gender=Gender.male, roles=[Role.admin]),
    User(id=UUID("f47ac10b-58cc-4372-a567-0e02b2c3d480"), first_name="Jane", last_name="Doe", middle_name="Doe", gender=Gender.female, roles=[Role.admin, Role.user])
]

@app.get("/")
async def read_root():
    return {"Hello": "mundo"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"user_id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
    # return {"message": "User not found"}

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user: UserUpdateRequest):
    for u in db:
        if u.id == user_id:
            if user.first_name is not None and user.first_name != "":
                u.first_name = user.first_name
            if user.last_name is not None and user.last_name != "":
                u.last_name = user.last_name
            if user.middle_name is not None and user.middle_name != "":
                u.middle_name = user.middle_name
            if user.gender is not None:
                u.gender = user.gender
            if user.roles is not None:
                u.roles = user.roles            
            return {"message": "User updated"}
    raise HTTPException(status_code=404, detail="User not found")
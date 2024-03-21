# Modello Pydantic per gli utenti
from typing import Dict
from fastapi import HTTPException, Request
from pydantic import BaseModel

from micropy.core import HttpMethod, MicroserviceBuilder


class User(BaseModel):
    id: int
    name: str

# Database fittizio
users_db: Dict[int, User] = {0:'enrico',1:'giulio'}

def create_app():
    # Funzioni per le operazioni CRUD
    async def create_user(request: Request):
        user = await request.json()
        if user['id'] in users_db:
            raise HTTPException(status_code=400, detail="User already exists")
        users_db[user['id']] = User(**user)
        return users_db[user['id']]

    async def get_user(request: Request, user_id: int):
        if user_id not in users_db:
            raise HTTPException(status_code=404, detail="User not found")
        return users_db[user_id]

    async def update_user(request: Request, user_id: int):
        if user_id not in users_db:
            raise HTTPException(status_code=404, detail="User not found")
        user_update = await request.json()
        users_db[user_id].name = user_update['name']
        return users_db[user_id]

    async def delete_user(request: Request, user_id: int):
        if user_id not in users_db:
            raise HTTPException(status_code=404, detail="User not found")
        del users_db[user_id]
        return {"message": "User deleted"}

    # Creazione e configurazione del microservizio
    builder = MicroserviceBuilder()
    app = (builder
        .add_endpoint(path="/users", method=HttpMethod.POST, func=create_user)
        .add_endpoint(path="/users/{user_id}", method=HttpMethod.GET, func=get_user)
        .add_endpoint(path="/users/{user_id}", method=HttpMethod.PUT, func=update_user)
        .add_endpoint(path="/users/{user_id}", method=HttpMethod.DELETE, func=delete_user)
        .build())
    return app
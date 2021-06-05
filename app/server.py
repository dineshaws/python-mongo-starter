from fastapi import FastAPI

from app.infrastructure.config.db_connection import Database
from app.interfaces.controllers.controller_factory import ControllerFactory
from app.infrastructure.config.enum.controller import get_controller_enum
from app.entities.user import User

app = FastAPI()

Database.initialize()

type = get_controller_enum('UserController')
user_controller = ControllerFactory().create(type)

@app.get('/', status_code=200)
def get_root():
    return {'Foo': 'BAR'}

@app.get('/api/v1/users', status_code= 200)
def get_users():
    return [{'id': 1}, {'id': 2}]

@app.get('/api/v1/users/{user_id}', status_code= 200)
def get_user(user_id: int):
    return user_controller.get(user_id)

@app.post('/api/v1/users', status_code=201)
def create_user(user: User):
    user_controller.create(user)
    return {'message': 'success'}

@app.put('api/v1/users/{user_id}', status_code= 200)
def edit_user(user_id: int, user: User):
    return user
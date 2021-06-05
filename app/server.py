from fastapi import FastAPI

from app.entities.user import User
from app.db_connection import Database


app = FastAPI()

Database.initialize()

@app.get('/', status_code=200)
def get_root():
    return {'Foo': 'BAR'}

@app.get('/api/v1/users', status_code= 200)
def get_users():
    return [{'id': 1}, {'id': 2}]

@app.get('/api/v1/users/{user_id}', status_code= 200)
def get_user(user_id: int):
    return Database.find_one('user', {'id': user_id})

@app.post('/api/v1/users', status_code=201)
def create_user(user: User):
    print('afer user ', user)
    print('afer user ', type(user))
    Database.insert_one('user', user)
    return {'msg': 'success'}

@app.put('api/v1/users/{user_id}', status_code= 200)
def edit_user(user_id: int, user: User):
    return user
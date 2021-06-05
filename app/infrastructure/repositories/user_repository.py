from app.infrastructure.repositories.base_repository import BaseRepository
from app.entities.user import User


class UserRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(collection='user')

    def find_user(self, user_id):
        query = {'id': user_id}
        params = {'_id' : 0 }
        data = self.find_one(query, params)
        if data:
            return User(**data)
        else:
            raise Exception('User not found')
    
    def create_user(self, user_data):
        data = self.insert_one(user_data)
        return data
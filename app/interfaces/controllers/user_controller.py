from app.interfaces.controllers.base_controller import BaseController
from app.infrastructure.repositories.user_repository import UserRepository

class UserController(BaseController):
    def __init__(self) -> None:
        super().__init__()
        self.UserRepository = UserRepository()

    def create(self, data):
        return self.UserRepository.create_user(data)

    def get(self, user_id):
        return self.UserRepository.find_user(user_id)
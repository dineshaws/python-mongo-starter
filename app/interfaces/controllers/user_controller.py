from app.interfaces.controllers.base_controller import BaseController

from app.use_cases.users.create_user_use_case import CreateUserUseCase
from app.use_cases.users.get_user_use_case import GetUserUseCase

class UserController(BaseController):
    def __init__(self) -> None:
        super().__init__()

    def create(self, data):
        return CreateUserUseCase().execute(data)

    def get(self, user_id):
        return GetUserUseCase().execute(user_id)
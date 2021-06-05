from app.use_cases.base_use_case import BaseUseCase

from app.infrastructure.repositories.user_repository import UserRepository

class GetUserUseCase(BaseUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.userRepository = UserRepository()

    def execute(self, user_id):
        return self.userRepository.find_user(user_id)
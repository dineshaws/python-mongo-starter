from app.use_cases.base_use_case import BaseUseCase


from app.infrastructure.repositories.user_repository import UserRepository

class CreateUserUseCase(BaseUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.userRepository = UserRepository()

    def execute(self, data):
        return self.userRepository.create_user(data)
from app.use_cases.base_use_case import BaseUseCase

class CreateUserUseCase(BaseUseCase):
    def __init__(self, user_repo) -> None:
        super().__init__()
        self.user_repo = user_repo

    def execute(self, data):
        return user_repo.create(data)
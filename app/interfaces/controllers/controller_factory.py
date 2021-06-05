from app.infrastructure.config.enum.controller import get_controller_enum

from app.interfaces.controllers.user_controller import UserController


class ControllerFactory():
    def __init__(self) -> None:
        pass
    def create(self, type):
        if type == get_controller_enum('UserController'):
            return UserController()

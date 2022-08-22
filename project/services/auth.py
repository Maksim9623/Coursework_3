from os import abort

from project.dao.auth import AuthDAO
from project.exceptions import UserNotFound, WrongPassword
from project.services.base import BaseService
from project.tools.security import generate_password_hash, compare_password, generate_tokens, update_refresh_token


class AuthService(BaseService):
    def register(self,  email, password):
        # Хэшируем пароль
        password_hash = generate_password_hash(password=password)
        # Создает пользователя
        return self.dao.create(email=email, password_hash=password_hash)

    def login(self, email, password):
        user = self.dao.get_user_by_email(email=email)
        if user is None:
            raise UserNotFound

        password_hash = generate_password_hash(password)
        if not compare_password(user['password_hash'], password_hash):
            raise WrongPassword

        return generate_tokens(user)

    def approve_refresh_token(self, refresh_token):
        data = update_refresh_token(refresh_token)
        email = data.get('email')

        user = self.dao.get_user_by_email(email=email)
        if user is None:
            abort()

        return generate_tokens(user)

    @staticmethod
    def get_data_from_token(refresh_token):
        data = update_refresh_token(refresh_token)
        return data






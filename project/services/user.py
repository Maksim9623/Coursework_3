from project.dao.models.user import User
from project.exceptions import ItemNotFound
from project.services.base import BaseService
from project.tools.security import update_refresh_token


class UsersService(BaseService):
    def get_item(self, pk):
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page):
        return self.dao.get_all(page=page)

    @staticmethod
    def get_data_from_token(refresh_token):
        data = update_refresh_token(refresh_token)
        return data

    def get_by_token(self, refresh_token):
        data = self.get_data_from_token(refresh_token)

        if data:
            return self.dao.get_by_email(data.get('email'))

    def update_user(self, data, refresh_token):
        user = self.get_by_token(refresh_token)

        if user:
            self.dao.update(email=user.email, data=data)

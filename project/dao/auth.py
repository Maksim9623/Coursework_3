from sqlalchemy.orm import scoped_session

from project.dao.base import BaseDAO
from project.dao.models.user import User, UserSchema


class AuthDAO(BaseDAO):

    def __init__(self, db_session: scoped_session):
        super().__init__(db_session)
        self.session = None

    def create(self, email, password):
        new_user = User(
            email=email,
            password=password,
        )
        self.session.add(new_user)
        self.session.commit()

        return UserSchema().dump(new_user)
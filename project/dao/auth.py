from sqlalchemy.orm import scoped_session

from project.dao.base import BaseDAO
from project.dao.models.user import User, AuthUserSchema, UserSchema


class AuthDAO(BaseDAO):

    def create(self, email, password_hash):
        new_user = User(
            email=email,
            password_hash=password_hash,
        )
        self._db_session.add(new_user)
        self._db_session.commit()

        return AuthUserSchema().dump(new_user)

    def get_user_by_email(self, email):
        user = self._db_session.query(
            User,
        ).filter(
            User.email == email,
        ).one_or_none()

        if user is not None:
            return AuthUserSchema().dump(user)

        return None


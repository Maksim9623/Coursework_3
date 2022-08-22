from project.dao import AuthDAO, UserDAO
from project.dao.main_dao import GenresDAO, DirectorsDAO, MoviesDAO
from project.services import GenreService, MovieService, AuthService, UsersService
from project.services.director import DirectorsService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
auth_dao = AuthDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenreService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
auth_service = AuthService(dao=auth_dao)
user_service = UsersService(dao=user_dao)


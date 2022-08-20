from project.dao import GenreDAO, MovieDAO, DirectorDAO

from project.services import GenreService, DirectorService, MovieService
from project.setup.db import db

# DAO
genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)

# Services
genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)

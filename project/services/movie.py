from typing import Optional

from project.dao import MoviesDAO
from project.dao.models.movie import Movie
from project.exceptions import ItemNotFound


class MovieService:
    def __init__(self, dao: MoviesDAO):
        self.dao = dao

    def get_one(self, pk):
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, filter=None, page: Optional[int] = None) -> list[Movie]:
        return self.dao.get_fresh(page=page, filter=filter)

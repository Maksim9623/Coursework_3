from typing import Optional

from project.dao import MoviesDAO
from project.dao.models.movie import Movie


class MovieService:
    def __init__(self, dao: MoviesDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_by_id(mid)

    def get_all(self, filter=None, page: Optional[int] = None) -> list[Movie]:
        return self.dao.get_fresh(page=page, filter=filter)

from project.dao.base import BaseDAO
# from project.dao.genre import GenreDAO
from project.exceptions import ItemNotFound


class GenreService:
    def __init__(self, dao: BaseDAO):
        self.dao = dao

    def get_item(self, pk):
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page):
        return self.dao.get_all(page=page)


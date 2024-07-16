from services.import_movies import ImportMoviesService
from services.add_movie import AddMovieService
from services.delete_movie import DeleteMovieService
from services.get_movie import GetMovieService
from services.list_movies import ListMoviesService
from services.search_movies import SearchMoviesService

class MovieController:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def import_from_csv(self, file):
        service = ImportMoviesService(self.movie_repository)
        return service.import_from_csv(file)

    def import_from_doc(self, file):
        service = ImportMoviesService(self.movie_repository)
        return service.import_from_doc(file)

    def import_from_txt(self, file):
        service = ImportMoviesService(self.movie_repository)
        return service.import_from_txt(file)

    def list_movies(self):
        return self.movie_repository.list()

    def add_movie(self, title, year, format, actors):
        code = secrets.token_hex(5)
        service = AddMovieService(self.movie_repository)
        return service.execute(code, title, year, format, actors)

    def delete_movie(self, code):
        service = DeleteMovieService(self.movie_repository)
        return service.execute(code)

    def get_movie(self, code):
        service = GetMovieService(self.movie_repository)
        return service.execute(code)

    def sort_movies(self):
        service = ListMoviesService(self.movie_repository)
        return service.execute()

    def search_by_title(self, title):
        service = SearchMoviesService(self.movie_repository)
        return service.search_by_title(title)

    def search_by_actor(self, actor):
        service = SearchMoviesService(self.movie_repository)
        return service.search_by_actor(actor)

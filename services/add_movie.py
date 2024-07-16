from entities.movie import Movie

class AddMovieService:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def execute(self, code, title, year, format, actors):
        movie = Movie(code, title, year, format, actors)
        self.movie_repository.add(movie)

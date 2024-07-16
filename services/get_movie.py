class GetMovieService:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def execute(self, code):
        return self.movie_repository.get(code)

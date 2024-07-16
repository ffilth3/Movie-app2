class DeleteMovieService:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def execute(self, code):
        self.movie_repository.delete(code)

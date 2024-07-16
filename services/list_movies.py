class ListMoviesService:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def execute(self):
        movies = self.movie_repository.list()
        return sorted(movies, key=lambda movie: movie.title.lower())

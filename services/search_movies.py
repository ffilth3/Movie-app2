class SearchMoviesService:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def search_by_title(self, title):
        return self.movie_repository.search_by_title(title)

    def search_by_actor(self, actor):
        return self.movie_repository.search_by_actor(actor)

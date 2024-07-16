from entities.movie import Movie
from frameworks.sqlalchemy_config import db, MovieModel

class SQLAlchemyMovieRepository:
    def add(self, movie):
        db_movie = MovieModel(
            code=movie.code,
            title=movie.title,
            year=movie.year,
            format=movie.format,
            actors=movie.actors
        )
        db.session.add(db_movie)
        db.session.commit()

    def get_by_title(self, title):
        movie = MovieModel.query.filter_by(title=title).first()
        if movie:
            return Movie(
                code=movie.code,
                title=movie.title,
                year=movie.year,
                format=movie.format,
                actors=movie.actors
            )
        return None

    def list(self):
        movies = MovieModel.query.all()
        return [
            Movie(
                code=movie.code,
                title=movie.title,
                year=movie.year,
                format=movie.format,
                actors=movie.actors
            )
            for movie in movies
        ]

    def delete(self, code):
        movie = MovieModel.query.filter_by(code=code).first()
        if movie:
            db.session.delete(movie)
            db.session.commit()

    def get(self, code):
        movie = MovieModel.query.filter_by(code=code).first()
        if movie:
            return Movie(
                code=movie.code,
                title=movie.title,
                year=movie.year,
                format=movie.format,
                actors=movie.actors
            )
        return None

    def search_by_title(self, title):
        movies = MovieModel.query.filter(MovieModel.title.ilike(f'%{title}%')).all()
        return [
            Movie(
                code=movie.code,
                title=movie.title,
                year=movie.year,
                format=movie.format,
                actors=movie.actors
            )
            for movie in movies
        ]

    def search_by_actor(self, actor):
        movies = MovieModel.query.filter(MovieModel.actors.ilike(f'%{actor}%')).all()
        return [
            Movie(
                code=movie.code,
                title=movie.title,
                year=movie.year,
                format=movie.format,
                actors=movie.actors
            )
            for movie in movies
        ]

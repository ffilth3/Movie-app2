from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from adapters.controllers.movie_controller import MovieController
from adapters.repositories.movie_repository import SQLAlchemyMovieRepository

movie_router = Blueprint('movie_router', __name__)
movie_repository = SQLAlchemyMovieRepository()
movie_controller = MovieController(movie_repository)

@movie_router.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        year = int(request.form['year'])
        format = request.form['format']
        actors = request.form['actors']
        movie_controller.add_movie(title, year, format, actors)
        return redirect(url_for('movie_router.index'))
    movies = movie_controller.list_movies()
    return render_template('index.html', movies=movies)

@movie_router.route('/sort', methods=['GET'])
def sort_movies():
    movies = movie_controller.list_movies()
    return render_template('index.html', movies=movies)

@movie_router.route('/delete/<string:code>', methods=['GET'])
def delete(code):
    movie_controller.delete_movie(code)
    return redirect(url_for('movie_router.index'))

@movie_router.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        movies = movie_controller.search_movies(query)
        return render_template('search.html', movies=movies)
    return render_template('search.html')

@movie_router.route('/movies/<string:code>', methods=['GET'])
def get_movie(code):
    movie = movie_controller.get_movie(code)
    if movie:
        return render_template('movie.html', movie=movie)
    return jsonify({'message': 'Movie not found'}), 404

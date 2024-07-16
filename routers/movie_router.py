from flask import Blueprint, render_template, request, redirect, url_for
from adapters.controllers.movie_controller import MovieController
from adapters.repositories.movie_repository import SQLAlchemyMovieRepository
import secrets

movie_router = Blueprint('movie_router', __name__)
movie_repository = SQLAlchemyMovieRepository()
movie_controller = MovieController(movie_repository)

@movie_router.route('/', methods=['GET'])
def index():
    movies = movie_controller.list_movies()
    return render_template('index.html', movies=movies)

@movie_router.route('/import', methods=['GET', 'POST'])
def import_movies():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            if file.filename.endswith('.csv'):
                movies = movie_controller.import_from_csv(file)
            elif file.filename.endswith('.doc') or file.filename.endswith('.docx'):
                movies = movie_controller.import_from_doc(file)
            elif file.filename.endswith('.txt'):
                movies = movie_controller.import_from_txt(file)
            else:
                return 'Будь ласка, завантажте файл у форматі CSV, DOC/DOCX або TXT', 400

            if movies:
                return redirect(url_for('movie_router.index'))
            else:
                return "Не вдалося імпортувати фільми", 400
        else:
            return "Файл не завантажено", 400

    return render_template('import.html')

@movie_router.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        format = request.form['format']
        actors = request.form['actors']
        movie_controller.add_movie(title, year, format, actors)
        return redirect(url_for('movie_router.index'))
    return render_template('add_movie.html')

@movie_router.route('/delete/<string:code>', methods=['GET'])
def delete_movie(code):
    movie_controller.delete_movie(code)
    return redirect(url_for('movie_router.index'))

@movie_router.route('/movie/<string:code>', methods=['GET'])
def get_movie(code):
    movie = movie_controller.get_movie(code)
    return render_template('movie.html', movie=movie)

@movie_router.route('/sort', methods=['GET'])
def sort_movies():
    movies = movie_controller.sort_movies()
    return render_template('index.html', movies=movies)

@movie_router.route('/search', methods=['GET', 'POST'])
def search_movies():
    if request.method == 'POST':
        query = request.form['query']
        search_by = request.form['search_by']
        if search_by == 'title':
            movies = movie_controller.search_by_title(query)
        elif search_by == 'actor':
            movies = movie_controller.search_by_actor(query)
        return render_template('index.html', movies=movies)
    return render_template('search.html')

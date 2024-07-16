import csv
import docx
from io import StringIO
import secrets
import re
from entities.movie import Movie

class ImportMoviesService:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def import_from_csv(self, file):
        movies = []
        try:
            file_contents = file.read().decode('utf-8')
            reader = csv.DictReader(StringIO(file_contents))
            for row in reader:
                self.add_movie(row['Назва'], row['Рік'], row['Формат'], row['Актори'], movies)
        except (ValueError, KeyError, UnicodeDecodeError) as e:
            print(f'Помилка під час завантаження CSV-файлу: {e}')
        except Exception as e:
            print(f'Невідома помилка під час завантаження CSV-файлу: {e}')
        return movies

    def import_from_doc(self, file):
        movies = []
        try:
            doc = docx.Document(file)
            for paragraph in doc.paragraphs:
                if paragraph.text.strip():
                    fields = self.split_line(paragraph.text)
                    if len(fields) >= 4:
                        self.add_movie(fields[0], fields[1], fields[2], fields[3], movies)
        except Exception as e:
            print(f'Помилка під час завантаження DOC/DOCX-файлу: {e}')
        return movies

    def import_from_txt(self, file):
        movies = []
        try:
            file_contents = file.read().decode('utf-8')
            for line in file_contents.splitlines():
                if line.strip():
                    fields = self.split_line(line.strip())
                    if len(fields) >= 4:
                        self.add_movie(fields[0], fields[1], fields[2], fields[3], movies)
        except Exception as e:
            print(f'Помилка під час завантаження TXT-файлу: {e}')
        return movies

    def add_movie(self, title, year, format, actors, movies):
        try:
            code = secrets.token_hex(5)
            existing_movie = self.movie_repository.get_by_title(title.strip())
            if not existing_movie:
                movie = Movie(
                    code=code,
                    title=title.strip(),
                    year=int(year.strip()),
                    format=format.strip(),
                    actors=actors.strip()
                )
                self.movie_repository.add(movie)
                movies.append(movie)
            else:
                print(f"Фільм з назвою {title.strip()} вже існує")
        except Exception as e:
            print(f'Помилка під час додавання фільму {title.strip()}: {e}')

    def split_line(self, line):
        # Роздільники: пробіл, кома, дві крапки, крапка з комою, вертикальна риса
        delimiters = r'\s+|,|:|;|\|'
        return re.split(delimiters, line)

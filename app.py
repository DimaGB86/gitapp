from flask import Flask  # type: ignore
import random
from datetime import datetime, timedelta
import os

# Создаем экземпляр приложения
app = Flask(__name__)

# Глобальный список пород кошек
CAT_BREEDS = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
# Получаем абсолютный путь к папке проекта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Путь к файлу с книгой
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')


# Определяем маршрут для главной страницы
@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars_list():
    cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
    return ', '.join(cars)


@app.route('/cats')
def get_random_cat_breed():
    breed = random.choice(CAT_BREEDS)
    return f"Случайная порода кошки: {breed}"


@app.route('/get_time/now')
def get_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Точное время: {current_time}"


@app.route('/get_time/future')
def get_future_time():
    current_time = datetime.now()
    future_time = current_time + timedelta(hours=1)
    formatted_future_time = future_time.strftime("%H:%M:%S")
    return f"Точное время через час будет {formatted_future_time}"


# Функция для получения списка слов из файла
def get_words_from_file(file_path):
    with open(file_path, encoding="utf-8") as file:
        content = file.read()
        words = content.split()
        return words


# Загружаем слова из файла только один раз
words = get_words_from_file(BOOK_FILE)


@app.route('/get_random_word')
def get_random_word():
    word = random.choice(words)
    return f'Случайное слово: {word}'


@app.route('/counter')
def hello_world():
    return 'Hello, World!'


# Запускаем приложение
if __name__ == '__main__':
    app.run(debug=True)

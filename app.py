from flask import Flask
from routes import handle_index_request  # Імпорт функції для обробки запитів

app = Flask(__name__)  # Створення екземпляра Flask додатка


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Основний маршрут програми.
    Приймає GET і POST запити на кореневий URL.
    """
    return handle_index_request()  # Виклик функції обробки індексного запиту


if __name__ == '__main__':
    app.run(debug=False)
    # Запуск програми Flask

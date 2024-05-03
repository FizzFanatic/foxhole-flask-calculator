from flask import render_template, redirect, request, url_for
from converters import cement_mixer_func, forge_func, materials_factory_func, processing_station


def handle_cement_mixer_request():
    try:
        # Отримуємо значення amount з форми і перетворюємо його на ціле число
        amount = int(request.form['amount'])
        # Перевіряємо, чи знаходиться значення amount в діапазоні від 1 до 100000
        if not 1 <= amount <= 100000:
            # Якщо значення поза діапазоном, повертаємо шаблон із повідомленням про помилку
            return render_template('index.html', error_message_cement_mixer="Значення має бути між 1 і 100000")
    except ValueError:
        # Якщо виникає виняток ValueError (некоректне число), повертаємо шаблон із повідомленням про помилку
        return render_template('index.html', error_message_cement_mixer="Введіть коректне число для розрахунку")

    # Виконуємо розрахунок з використанням функції cement_mixer_calculator
    result = cement_mixer_func.cement_mixer_calculator(amount)
    if result:
        # Якщо результат розрахунку існує, повертаємо шаблон із результатом
        return render_template('index.html', cement_mixer_result=result)


def handle_materials_factory_request():
    # Отримуємо дані з форми
    from_resource = request.form['from_resource']
    try:
        # Намагаємося перетворити значення amount на ціле число
        amount = int(request.form['amount'])
        # Перевіряємо, чи знаходиться значення amount в діапазоні від 1 до 100000
        if not 1 <= amount <= 100000:
            # Якщо значення поза діапазоном, повертаємо шаблон із повідомленням про помилку
            return render_template('index.html', error_message_materials_factory="Значення має бути між 1 і 100000")
    except ValueError:
        # Якщо виникає виняток ValueError (некоректне число), повертаємо шаблон із повідомленням про помилку
        return render_template('index.html',
                               error_message_materials_factory="Введіть коректне число для розрахунку")

    # Виконуємо розрахунок з використанням функції calculate_conversion
    result = materials_factory_func.calculate_conversion(from_resource, amount)
    if result:
        # Якщо результат розрахунку існує, повертаємо шаблон із результатом
        return render_template('index.html', materials_factory_result=result)


def handle_forge_request():
    # Отримуємо дані з форми
    from_resource = request.form['from_resource']
    try:
        # Намагаємося перетворити значення amount на ціле число
        amount = int(request.form['amount'])
        # Перевіряємо, чи знаходиться значення amount в діапазоні від 1 до 100000
        if not 1 <= amount <= 100000:
            # Якщо значення поза діапазоном, повертаємо шаблон із повідомленням про помилку
            return render_template('index.html', error_message_forge="Значення має бути між 1 і 100000")
    except ValueError:
        # Якщо виникає виняток ValueError (некоректне число), повертаємо шаблон із повідомленням про помилку
        return render_template('index.html',
                               error_message="Введіть коректне число для розрахунку")

    # Виконуємо розрахунок з використанням функції calculate_conversion_forge
    result = forge_func.calculate_conversion_forge(from_resource, amount)
    if result:
        # Якщо результат розрахунку існує, повертаємо шаблон із результатом
        return render_template('index.html', forge_result=result)


def handle_processing_station_request():
    # Отримуємо дані з форми
    from_resource = request.form['from_resource']
    try:
        # Намагаємося перетворити значення amount на ціле число
        amount = int(request.form['amount'])
        # Перевіряємо, чи знаходиться значення amount в діапазоні від 1 до 100000
        if not 1 <= amount <= 100000:
            # Якщо значення поза діапазоном, повертаємо шаблон із повідомленням про помилку
            return render_template('index.html',
                                   error_message_processing_station="Значення має бути між 1 і 100000")
    except ValueError:
        # Якщо виникає виняток ValueError (некоректне число), повертаємо шаблон із повідомленням про помилку
        return render_template('index.html',
                               error_message_processing_station="Введіть коректне число для розрахунку")

    # Виконуємо розрахунок з використанням функції processing_station_calculator
    result = processing_station.processing_station_calculator(from_resource, amount)
    if result:
        # Якщо результат розрахунку існує, повертаємо шаблон із результатом
        return render_template('index.html', processing_station_result=result)


def handle_index_request():
    # Перевіряємо, чи був відправлений POST-запит
    if request.method == 'POST':
        # Якщо POST-запит, перевіряємо, яку кнопку було натиснуто у формі
        if "cement_mixer" in request.form:
            # Якщо натиснута кнопка "cement_mixer", викликаємо функцію для обробки цього запиту
            return handle_cement_mixer_request()

        elif "reset" in request.form:
            # Якщо натиснута кнопка "reset", перенаправляємо користувача на головну сторінку
            return redirect(url_for('index'))

        elif "materials_factory" in request.form:
            # Якщо натиснута кнопка "materials_factory", викликаємо функцію для обробки цього запиту
            return handle_materials_factory_request()

        elif "forge" in request.form:
            # Якщо натиснута кнопка "forge", викликаємо функцію для обробки цього запиту
            return handle_forge_request()

        elif "processing_station" in request.form:
            # Якщо натиснута кнопка "processing_station", викликаємо функцію для обробки цього запиту
            return handle_processing_station_request()
    # Якщо запит не є POST-запитом або жодна з кнопок не була натиснута, відображаємо головну сторінку
    return render_template('index.html')


import math


def processing_station_calculator(from_resource, amount):
    if from_resource == "Металлолом/Биматы":
        if isinstance(amount, int):
            metal_consumption_one = 1 / 2 # 1 базовий матеріал = 2 металлолома
            production = round(metal_consumption_one * amount)

            all_boxes = math.floor(production / 100)
            dunne_boxes = math.ceil(all_boxes / 15)
            flatbedboxes = math.ceil(all_boxes / 60)

            html_response = f"""
            <div id="result_page">
                <h3>Результати розрахунку:</h3>
                <p>Буде використано Металлолом: <span class="number">{amount}</span></p>
                <p>Буде вироблено ресурсу Базові матеріали: <span class="number">{production}</span></p>
                <p>Базові матеріали в ящиках: <span class="number">{all_boxes}</span></p>
                <p>Для перевезення цих ящиків вам знадобиться: <span class="number">{dunne_boxes}</span> машина(и) Dunne або ж <span class="number">{flatbedboxes}</span> Flatbed</p>
                <button onclick="window.location.href='/'" class="btn_restart">Скинути результат конвертації</button>
            </div>"""

            return html_response

        return None

    elif from_resource == "Металлолом/Дизель":
        if isinstance(amount, int):
            diesel_one = 1 / 10
            production = round(diesel_one * amount)

            all_boxes = math.floor(production / 1)
            dunne_boxes = math.ceil(all_boxes / 15)
            flatbedboxes = math.ceil(all_boxes / 60)

            html_response = f"""
            <div id="result_page">
                <h3>Результати розрахунку:</h3>
                <p>Буде використано Металлолом: <span class="number">{amount}</span></p>
                <p>Буде вироблено ресурсу Дизель: <span class="number">{production}</span></p>
                <p>Дизель в ящиках: <span class="number">{all_boxes}</span></p>
                <p>Для перевезення цих ящиків вам знадобиться: <span class="number">{dunne_boxes}</span> машина(и) Dunne або ж <span class="number">{flatbedboxes}</span> Flatbed</p>
                <button onclick="window.location.href='/'" class="btn_restart">Скинути результат конвертації</button>
            </div>"""

            return html_response

        return None

    elif from_resource == "Металлолом/ВзрывчатыеМатериалы":
        if isinstance(amount, int):
            diesel_one = 1 / 10
            production = round(diesel_one * amount)

            all_boxes = math.floor(production / 20)
            dunne_boxes = math.ceil(all_boxes / 15)
            flatbedboxes = math.ceil(all_boxes / 60)

            html_response = f"""
            <div id="result_page">
                <h3>Результати розрахунку:</h3>
                <p>Буде використано Металлолом: <span class="number">{amount}</span></p>
                <p>Буде вироблено ресурсу Вибухові матеріали: <span class="number">{production}</span></p>
                <p>Вибухові матеріали в ящиках: <span class="number">{all_boxes}</span></p>
                <p>Для перевезення цих ящиків вам знадобиться: <span class="number">{dunne_boxes}</span> машина(и) Dunne або ж <span class="number">{flatbedboxes}</span> Flatbed</p>
                <button onclick="window.location.href='/'" class="btn_restart">Скинути результат конвертації</button>
            </div>"""

            return html_response

        return None

    elif from_resource == "Компоненты/Рафинированные материалы":
        if isinstance(amount, int):
            diesel_one = 1 / 20
            production = round(diesel_one * amount)

            all_boxes = math.floor(production / 20)
            dunne_boxes = math.ceil(all_boxes / 15)
            flatbedboxes = math.ceil(all_boxes / 60)

            html_response = f"""
            <div id="result_page">
                <h3>Результати розрахунку:</h3>
                <p>Буде використано Металлолом: <span class="number">{amount}</span></p>
                <p>Буде вироблено ресурсу Вибухові матеріали: <span class="number">{production}</span></p>
                <p>Вибухові матеріали в ящиках: <span class="number">{all_boxes}</span></p>
                <p>Для перевезення цих ящиків вам знадобиться: <span class="number">{dunne_boxes}</span> машина(и) Dunne або ж <span class="number">{flatbedboxes}</span> Flatbed</p>
                <button onclick="window.location.href='/'" class="btn_restart">Скинути результат конвертації</button>
            </div>"""

            return html_response

        return None

def calculate_conversion(from_resource, amount):
    # Розраховує конвертацію для обраного ресурсу

    if from_resource == "Припаси обслуговування":
        if isinstance(amount, int):
            # Розрахунок конвертації для припасів обслуговування

            cycle = amount / 20  # Визначаємо кількість циклів
            general_time_sec = cycle * 25  # Розраховуємо загальний час виробництва (у секундах)

            # Визначення одиниці вимірювання часу
            time_map = "секунди"
            if general_time_sec >= 60:
                time_translation = general_time_sec / 60  # Переводимо секунди у хвилини
                general_time_sec = time_translation
                time_map = "хвилини"
                if time_translation >= 60:
                    general_time_sec = time_translation / 60
                    time_map = "години"
            else:
                pass

            general_time_sec = round(general_time_sec, 2)  # Округлюємо час до двох знаків після коми

            metal_consumption_one = 100 / 20  # Витрата металу на одну флягу
            all_metal = amount * metal_consumption_one  # Загальна витрата металу

            return {
                'metal_scraps': all_metal,
                'produced_resource': amount,
                'time_spent': general_time_sec,
                'time_map': time_map
            }

        return None

    elif from_resource == "Будівельні матеріали":
        if isinstance(amount, int):
            # Розрахунок конвертації для будівельних матеріалів

            cycle = amount / 1  # Визначаємо кількість циклів
            general_time_sec = cycle * 25  # Розраховуємо загальний час виробництва (у секундах)

            # Визначення одиниці вимірювання часу
            time_map = "секунди"
            if general_time_sec >= 60:
                time_translation = general_time_sec / 60  # Переводимо секунди у хвилини
                general_time_sec = time_translation
                time_map = "хвилини"
            else:
                pass

            metal_consumption_one = 10 / 1  # Витрата металу на один будівельний матеріал
            all_metal = amount * metal_consumption_one  # Загальна витрата металу
            general_time_sec = round(general_time_sec, 2)  # Округлюємо час до двох знаків після коми

            return {
                'metal_scraps': all_metal,
                'produced_resource': amount,
                'time_spent': general_time_sec,
                'time_map': time_map
            }

        return None

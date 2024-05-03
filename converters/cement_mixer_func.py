def cement_mixer_calculator(amount):
    if isinstance(amount, int):
        production_time_for_one_bag = 20  # Час у секундах для виробництва одного мішка цементу
        total_production_time = production_time_for_one_bag * amount  # Загальний час у секундах для виробництва вказаної кількості мішків цементу

        # Змінна для часової мітки
        time_label = "Секунди"
        if total_production_time >= 60:
            total_production_time /= 60  # Конвертація часу з секунд у хвилини
            time_label = "Хвилини"
            if total_production_time >= 60:
                total_production_time /= 60  # Конвертація часу з хвилин у години
                time_label = "Години"

        # Округлення часу до двох знаків після коми
        total_production_time = round(total_production_time, 2)

        # Кількість компонентів на один мішок цементу
        components_per_bag = 20  # Кількість компонентів, необхідних для виробництва одного мішка цементу
        total_components_required = components_per_bag * amount  # Загальна кількість компонентів, необхідних для виробництва вказаної кількості мішків цементу

        image_name = "CementMixerIcon.png"  # назва фото
        cement_produced = amount  # Кількість виробленого цементу

        return {
            'total_components_required': total_components_required,
            'cement_produced': cement_produced,
            'total_production_time': total_production_time,
            'time_label': time_label
        }

    return None

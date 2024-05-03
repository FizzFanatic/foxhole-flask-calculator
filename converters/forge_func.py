def calculate_conversion_forge(from_resource, amount):
    if from_resource == "Складальні матеріали 1":

        metal_per_unit = 15  # Використання металобрухту на 1 одиницю
        coking_coal_per_unit = 75  # Використання коксового вугілля на 1 одиницю

        the_amount_of_assembly_materials = amount  # Кількість сборочних матеріалів

        # загальна кількість металобрухту
        total_amount_of_scrap_metal = metal_per_unit * the_amount_of_assembly_materials
        # Загальна кількість коксового вугілля
        total_amount_coking_coal = coking_coal_per_unit * the_amount_of_assembly_materials

        production_time_in_minutes = 1  # час виробництва 1 одиниці у хвилинах

        total_time_in_minutes = production_time_in_minutes * amount

        time_label = "Хвилини"
        if total_time_in_minutes >= 60:
            total_time_in_minutes = round(total_time_in_minutes / 60, 2)
            time_label = "Години"
        else:
            pass

        return {
            "the_amount_of_assembly_materials": the_amount_of_assembly_materials,
            "total_amount_of_scrap_metal": total_amount_of_scrap_metal,
            "total_amount_coking_coal": total_amount_coking_coal,
            "total_time_in_minutes": total_time_in_minutes,
            "time_label": time_label,
            "name_res": "коксового вугілля"
        }

    elif from_resource == "Складальні матеріали 2":

        metal_per_unit = 15  # Використання металобрухту на 1 одиницю
        coking_coal_per_unit = 50  # Використання бензину на 1 одиницю

        the_amount_of_assembly_materials = amount  # Кількість сборочних матеріалів

        # загальна кількість металобрухту
        total_amount_of_scrap_metal = metal_per_unit * the_amount_of_assembly_materials
        # Загальна кількість коксового вугілля
        total_amount_coking_coal = coking_coal_per_unit * the_amount_of_assembly_materials

        production_time_in_minutes = 1  # час виробництва 1 одиниці у хвилинах

        total_time_in_minutes = production_time_in_minutes * amount

        time_label = "Хвилини"
        if total_time_in_minutes >= 60:
            total_time_in_minutes = round(total_time_in_minutes / 60, 2)
            time_label = "Години"
        else:
            pass

        return {
            "the_amount_of_assembly_materials": the_amount_of_assembly_materials,
            "total_amount_of_scrap_metal": total_amount_of_scrap_metal,
            "total_amount_coking_coal": total_amount_coking_coal,
            "total_time_in_minutes": total_time_in_minutes,
            "time_label": time_label,
            "name_res": "бензину"
        }

    return None

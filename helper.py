def get_ingredient_count(ingredients_list: list, ingredient_count_type: str) -> int:
    """В зависимости от параметра ingredient_count_type выбираем количество ингредиентов для заказа"""
    ingredients_count = len(ingredients_list)
    length_map = {
                "min": 1,
                "mean": ingredients_count // 2,
                "max": ingredients_count,
            }
    return length_map[ingredient_count_type]

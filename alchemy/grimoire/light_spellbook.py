from .light_validator import validate_ingredients


def light_spell_allowed_ingredients():
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str):
    res = validate_ingredients(ingredients)

    if "VALID" in res:
        return f"spell recorded:  {spell_name} ({res})"
    return f"spell rejected: {spell_name} ({res})"

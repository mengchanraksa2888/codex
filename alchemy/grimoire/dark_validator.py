from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):

    allow = dark_spell_allowed_ingredients()

    for item in allow:
        if item in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"

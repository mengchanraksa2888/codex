def validate_ingredients(ingredients: str):
    from .light_spellbook import light_spell_allowed_ingredients

    allow = light_spell_allowed_ingredients()

    for item in allow:
        if item in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"

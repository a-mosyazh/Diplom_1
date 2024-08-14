from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"

    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING

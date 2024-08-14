import pytest

from data import INGREDIENT_NAME, INGREDIENT_PRICE_FLOAT, INGREDIENT_PRICE_INTEGER
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:
    def test_ingredient_type_true(self, ingredient):
        assert ingredient.type == INGREDIENT_TYPE_SAUCE

    def test_name_of_bun_true(self, ingredient):
        assert ingredient.name == INGREDIENT_NAME

    def test_price_of_bun_true(self, ingredient):
        assert ingredient.price == INGREDIENT_PRICE_FLOAT

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == INGREDIENT_NAME

    @pytest.mark.parametrize(
        'price',
        [
            INGREDIENT_PRICE_FLOAT,
            INGREDIENT_PRICE_INTEGER
        ]
    )
    def test_get_price(self, ingredient, price):
        ingredient.price = price
        assert ingredient.get_price() == price

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

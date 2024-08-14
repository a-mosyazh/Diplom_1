from unittest.mock import Mock

import pytest

from data import BUN_NAME, BUN_PRICE_FLOAT, INGREDIENT_NAME, INGREDIENT_PRICE_FLOAT
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def bun():
    bun = Bun(name=BUN_NAME, price=BUN_PRICE_FLOAT)
    return bun


@pytest.fixture
def ingredient():
    ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name=INGREDIENT_NAME, price=INGREDIENT_PRICE_FLOAT)
    return ingredient


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Mock Bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Mock Ingredient"
    ingredient.get_type.return_value = "Mock Type"
    ingredient.get_price.return_value = 50.0
    return ingredient


@pytest.fixture
def database():
    database = Database()
    return database

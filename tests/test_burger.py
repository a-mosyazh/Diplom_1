from unittest.mock import Mock
from praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self, burger, mock_ingredient):
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 300.0

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert "(==== Mock Bun ====)" in receipt
        assert "= mock type Mock Ingredient =" in receipt
        assert "Price: 300.0" in receipt

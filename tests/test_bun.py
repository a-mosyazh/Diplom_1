import pytest

from data import BUN_NAME, BUN_PRICE_FLOAT, BUN_PRICE_INTEGER


class TestBun:

    def test_name_of_bun_true(self, bun):
        assert bun.name == BUN_NAME

    def test_price_of_bun_true(self, bun):
        assert bun.price == BUN_PRICE_FLOAT

    def test_get_name(self, bun):
        assert bun.get_name() == BUN_NAME

    @pytest.mark.parametrize(
        'price',
        [
            BUN_PRICE_FLOAT,
            BUN_PRICE_INTEGER
        ]
    )
    def test_get_price(self, bun, price):
        bun.price = price
        assert bun.get_price() == price

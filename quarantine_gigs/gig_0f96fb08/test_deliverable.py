import pytest
from model import calculate_bond_price, calculate_ytm


def test_calculate_bond_price():
    face_value = 1000
    coupon_rate = 0.05
    years_to_maturity = 10
    market_rate = 0.04
    expected_price = 1081.11
    assert (
        abs(
            calculate_bond_price(
                face_value, coupon_rate, years_to_maturity, market_rate
            )
            - expected_price
        )
        < 0.01
    )


def test_calculate_ytm():
    face_value = 1000
    coupon_rate = 0.05
    years_to_maturity = 10
    bond_price = 1081.11
    expected_ytm = 0.04
    assert (
        abs(
            calculate_ytm(face_value, coupon_rate, years_to_maturity, bond_price)
            - expected_ytm
        )
        < 0.01
    )


def test_calculate_bond_price_and_ytm():
    face_value = 1000
    coupon_rate = 0.05
    years_to_maturity = 10
    market_rate = 0.04
    bond_price = calculate_bond_price(
        face_value, coupon_rate, years_to_maturity, market_rate
    )
    ytm = calculate_ytm(face_value, coupon_rate, years_to_maturity, bond_price)
    assert abs(bond_price - 1081.11) < 0.01
    assert abs(ytm - 0.04) < 0.01

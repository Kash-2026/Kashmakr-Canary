import pytest
from model import calculate


def test_calculate_bond_price():
    data = {"faceValue": 1000, "couponRate": 5, "yearsToMaturity": 10, "marketRate": 5}
    result = calculate(data)
    assert result["bondPrice"] == 1000
    assert result["yieldToMaturity"] == 5


def test_calculate_bond_price_different_market_rate():
    data = {"faceValue": 1000, "couponRate": 5, "yearsToMaturity": 10, "marketRate": 6}
    result = calculate(data)
    assert result["bondPrice"] < 1000
    assert result["yieldToMaturity"] > 5


def test_calculate_bond_price_zero_coupon():
    data = {"faceValue": 1000, "couponRate": 0, "yearsToMaturity": 10, "marketRate": 5}
    result = calculate(data)
    assert result["bondPrice"] < 1000
    assert result["yieldToMaturity"] == 5

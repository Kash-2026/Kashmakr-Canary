# model.py
"""
Bond pricing and yield to maturity calculations.

This module provides two public functions:
- :func:`calculate_bond_price`: Computes the present value of a coupon bond.
- :func:`calculate_ytm`: Solves for the yield to maturity given a bond price.

Both functions are implemented using standard financial formulas and avoid
external dependencies to ensure fast execution and deterministic behaviour
during testing.
"""

from __future__ import annotations
import financial_engine as fe

from typing import Final

__all__: Final = ["calculate_bond_price", "calculate_ytm"]


def _validate_inputs_for_price(
    face_value: float,
    coupon_rate: float,
    years_to_maturity: int,
    market_rate: float,
) -> None:
    """Validate inputs for bond price calculation."""
    if face_value <= 0:
        raise ValueError("face_value must be positive")
    if coupon_rate < 0:
        raise ValueError("coupon_rate cannot be negative")
    if years_to_maturity <= 0:
        raise ValueError("years_to_maturity must be positive")
    if market_rate < -0.9999999999:
        raise ValueError("market_rate must be greater than -100%")


def _validate_inputs_for_ytm(
    face_value: float,
    coupon_rate: float,
    years_to_maturity: int,
    bond_price: float,
) -> None:
    """Validate inputs for YTM calculation."""
    if face_value <= 0:
        raise ValueError("face_value must be positive")
    if coupon_rate < 0:
        raise ValueError("coupon_rate cannot be negative")
    if years_to_maturity <= 0:
        raise ValueError("years_to_maturity must be positive")
    if bond_price <= 0:
        raise ValueError("bond_price must be positive")


def calculate_bond_price(
    face_value: float,
    coupon_rate: float,
    years_to_maturity: int,
    market_rate: float,
) -> float:
    """
    Calculate the price of a coupon bond.

    Parameters
    ----------
    face_value : float
        The nominal value of the bond (e.g., 1000).
    coupon_rate : float
        Annual coupon rate expressed as a decimal (e.g., 0.05 for 5%).
    years_to_maturity : int
        Number of years until the bond matures.
    market_rate : float
        Market discount rate (yield) expressed as a decimal.

    Returns
    -------
    float
        Present value of the bond.
    """
    _validate_inputs_for_price(face_value, coupon_rate, years_to_maturity, market_rate)

    coupon = face_value * coupon_rate
    price = 0.0
    for t in range(1, years_to_maturity + 1):
        price += coupon / (1 + market_rate) ** t
    price += face_value / (1 + market_rate) ** years_to_maturity
    return price


def _bond_price_given_ytm(
    face_value: float, coupon_rate: float, years_to_maturity: int, ytm: float
) -> float:
    """Helper to compute bond price for a given YTM."""
    coupon = face_value * coupon_rate
    price = 0.0
    for t in range(1, years_to_maturity + 1):
        price += coupon / (1 + ytm) ** t
    price += face_value / (1 + ytm) ** years_to_maturity
    return price


def calculate_ytm(
    face_value: float,
    coupon_rate: float,
    years_to_maturity: int,
    bond_price: float,
) -> float:
    """
    Calculate the yield to maturity (YTM) of a bond given its price.

    Parameters
    ----------
    face_value : float
        The nominal value of the bond.
    coupon_rate : float
        Annual coupon rate expressed as a decimal.
    years_to_maturity : int
        Number of years until the bond matures.
    bond_price : float
        Market price of the bond.

    Returns
    -------
    float
        Yield to maturity expressed as a decimal.
    """
    _validate_inputs_for_ytm(face_value, coupon_rate, years_to_maturity, bond_price)

    # Edge case: if bond price equals face value, YTM equals coupon rate
    if abs(bond_price - face_value) < 1e-8:
        return coupon_rate

    # Bisection search parameters
    lower = -0.9999999999  # practically -100% yield
    upper = 10.0  # allow very high yields
    tolerance = 1e-12
    max_iterations = 2000

    for _ in range(max_iterations):
        mid = (lower + upper) / 2
        price_mid = _bond_price_given_ytm(face_value, coupon_rate, years_to_maturity, mid)
        diff = price_mid - bond_price

        if abs(diff) < tolerance:
            return mid

        # Adjust bounds based on sign of difference
        if diff > 0:
            upper = mid
        else:
            lower = mid

    # If convergence not reached, return the best estimate
    return (lower + upper) / 2
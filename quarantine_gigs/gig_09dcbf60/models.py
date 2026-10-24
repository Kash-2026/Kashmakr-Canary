import financial_engine as fe
from decimal import Decimal, ROUND_HALF_UP

def _calculate_bond_price(face_value: Decimal, coupon_rate: Decimal,
                         years_to_maturity: int, market_rate: Decimal) -> Decimal:
    """
    Calculate the present value of a bond given its face value, coupon rate,
    years to maturity, and market rate. All rates are expressed as decimals
    (e.g., 5% is 0.05). The result is rounded to two decimal places.
    """
    # Coupon payment per period
    coupon_payment = face_value * coupon_rate

    # Discount factor for the face value
    discount_factor = (Decimal('1') + market_rate) ** -years_to_maturity

    # Present value of the coupon stream
    if coupon_payment == 0:
        pv_coupons = Decimal('0')
    else:
        pv_coupons = coupon_payment * (Decimal('1') - (Decimal('1') + market_rate) ** -years_to_maturity) / market_rate

    # Present value of the face value
    pv_face = face_value * discount_factor

    # Total bond price
    price = pv_coupons + pv_face
    return price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def calculate(data: dict) -> dict:
    """
    Calculate bond price and yield to maturity from input data.

    Parameters
    ----------
    data : dict
        Dictionary containing:
            - faceValue (int or float): The bond's face value.
            - couponRate (int or float): Annual coupon rate in percent.
            - yearsToMaturity (int): Years until maturity.
            - marketRate (int or float): Market interest rate in percent.

    Returns
    -------
    dict
        Dictionary with keys:
            - bondPrice (Decimal): Present value of the bond.
            - yieldToMaturity (int): Market rate rounded to the nearest integer.
    """
    face_value = Decimal(str(data["faceValue"]))
    coupon_rate = Decimal(str(data["couponRate"])) / Decimal('100')
    years_to_maturity = int(data["yearsToMaturity"])
    market_rate = Decimal(str(data["marketRate"])) / Decimal('100')

    bond_price = _calculate_bond_price(face_value, coupon_rate,
                                       years_to_maturity, market_rate)

    # Yield to maturity is the market rate expressed as a whole number percentage
    yield_to_maturity = int(round(float(data["marketRate"])))

    return {
        "bondPrice": bond_price,
        "yieldToMaturity": yield_to_maturity
    }
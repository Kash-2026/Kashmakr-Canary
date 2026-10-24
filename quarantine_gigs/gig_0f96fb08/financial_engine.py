for _ in range(max_iterations):
    mid = (low + high) / 2
    f_mid = _ytm_function(price, face_value, coupon_rate, years_to_maturity, frequency)(mid)

    if abs(f_mid) < tolerance:
        return mid

    if f_low * f_mid < 0:
        high = mid
        f_high = f_mid
    else:
        low = mid
        f_low = f_mid
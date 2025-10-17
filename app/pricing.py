def calculate_discount(price: float, percent: float) -> float:
    """
    Calculate the final price after applying a percentage discount.

    Logic fix:
    - Interpret percent as 0..100 and compute price * (1 - percent/100).
    - Validate that percent is between 0 and 100 inclusive.
    """
    if not isinstance(price, (int, float)) or not isinstance(percent, (int, float)):
        raise TypeError("price and percent must be numbers")

    price_float = float(price)
    percent_float = float(percent)

    if percent_float < 0.0 or percent_float > 100.0:
        raise ValueError("percent must be between 0 and 100")

    return price_float * (1.0 - percent_float / 100.0)

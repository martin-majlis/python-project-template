def divide(numerator: float, denominator: float) -> float:
    """
    Divides two numbers and returns result.

    :param numerator: numerator
    :param denominator: denominator
    :return: sum of two numbers

    >>> divide(4, 2)
    2.0
    >>> divide(4, -2)
    -2.0
    >>> divide(4, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return numerator / denominator

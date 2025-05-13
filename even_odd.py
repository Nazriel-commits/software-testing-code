def is_even_or_odd(n):
    """
    Determine whether an input integer is even or odd.
    Accepts integers or floats that represent whole numbers (e.g., 8.0)

    Args:
        n (int): The number to check.

    Returns:
        str: "even" if the number is even, "odd" if the number is odd.

    Raises:
        TypeError: If the input is not a numeric type or is a non-integer float
    """
    if isinstance(n, float):
        if not n.is_integer():
            raise TypeError("Float inputs must be whole numbers (e.g., 4.0)")
        n = int(n)
    elif not isinstance(n, int):
        raise TypeError("Input must be an integer or a whole number float")
    
    remainder = n % 2
    if remainder == 0:
        result = "even"
    else:
        result = "odd"
    return result 

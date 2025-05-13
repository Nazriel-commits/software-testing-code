def is_even_or_odd(n):
    """
    Determine whether an input integer is even or odd.

    Args:
        n (int): The number to check.

    Returns:
        str: "even" if the number is even, "odd" if the number is odd.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    remainder = n % 2
    if remainder == 0:
        result = "even"
    else:
        result = "odd"
    return result 
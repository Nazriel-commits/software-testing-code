def count_vowels(s):
    """
    Count the number of vowels in a string.

    Args:
        s (str): The string in which to count vowels.

    Returns:
        int: The number of vowels found in the string.

    Raises:
        TypeError: If the input is not a string.
    """
    
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    vowels = 'aeiouAEIOU'
    count = 0

    if len(s) == 0:
        return count
    
    for char in s:
        is_vowel = char in vowels 
        if is_vowel:
            count += 1
    return count
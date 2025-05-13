import pytest
from even_odd import is_even_or_odd 
from vowel_counter import count_vowels

def test_is_even_or_odd():
    # Test even/odd
    assert is_even_or_odd(2) == "even"
    assert is_even_or_odd(3) == "odd"
    # Test edge cases (zero, negative)
    assert is_even_or_odd(0) == "even"
    assert is_even_or_odd(-1) == "odd"
    # Test exception
    with pytest.raises(TypeError):
        is_even_or_odd("not a number")


def test_count_vowels():
    # Standard cases
    assert count_vowels("hello") == 2
    assert count_vowels("sky") == 0
    # Edge cases (empty string, all vowels)
    assert count_vowels("") == 0
    assert count_vowels("AEIOU") == 5
    # Test exception
    with pytest.raises(TypeError):
        count_vowels(123)
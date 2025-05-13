import pytest
from vowel_counter import count_vowels

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
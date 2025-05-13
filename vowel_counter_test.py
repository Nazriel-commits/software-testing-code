import pytest
from vowel_counter import count_vowels

def test_count_vowels():
    # Standard cases
    assert count_vowels("hello") == 2
    assert count_vowels("sky") == 0
    
    # Edge cases (empty string, all vowels)
    assert count_vowels("") == 0
    assert count_vowels("AEIOU") == 5

    # Mixed case
    assert count_vowels("aERoplAnE") == 5
    assert count_vowels("ZENbook") == 3

    # Special characters and numbers
    assert count_vowels("$e4t3d") == 1
    assert count_vowels("1llu$tr4te") == 2
    
    # Test exception
    with pytest.raises(TypeError):
        count_vowels(123)

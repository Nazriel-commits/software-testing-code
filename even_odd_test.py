import pytest
from even_odd import is_even_or_odd 

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

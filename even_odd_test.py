import pytest
from even_odd import is_even_or_odd 

def test_is_even_or_odd():
    # Test even/odd
    assert is_even_or_odd(2) == "even"
    assert is_even_or_odd(3) == "odd"
    
    # Test float handling - Flaots that represent whole numbers should be accepted
    assert is_even_or_odd(4.0) == "even"
    assert is_even_or_odd(12.000000) == "even"

    #Test non-integer float should raise an exception
    with pytest.raises(TypeError):
        is_even_or_odd(4.3)
    with pytest.raises(TypeError):
        is_even_or_odd(12.33453445)
        
    # Test edge cases (zero, negative)
    assert is_even_or_odd(0) == "even"
    assert is_even_or_odd(-1) == "odd"
    
    # Test exception for non-numberic inputs (string)
    with pytest.raises(TypeError):
        is_even_or_odd("not a number") 

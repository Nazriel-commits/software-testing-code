import pytest

@pytest.fixture
def sample_dict():
  return {"a": 1, "b": 2}

@pytest.mark.parametrize("x, y, result", [(1, 2, 3), (4, 5, 6)])
def test_add(x, y, result):
  assert x + y == result

from src.math_utils import multiply

def test_basic_math():
    assert 2+2 == 4

def test_multi():
    assert multiply(3,5) == 15, 'не верно отработала'
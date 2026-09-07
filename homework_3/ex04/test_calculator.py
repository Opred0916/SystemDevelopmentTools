from calculator import is_even


def test_even_number():
    assert is_even(8) is True


def test_odd_number():
    assert is_even(7) is False

    
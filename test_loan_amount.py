import pytest

def is_eligible(amount):
    return 10000 <= amount <= 500000


@pytest.mark.smoke
@pytest.mark.parametrize("amount, expected", [
    (9999, False),
    (10000, True),
    (10001, True),
    (500000, True),
    (500001, False),
])
def test_is_eligible(amount, expected):
    assert is_eligible(amount) == expected
    
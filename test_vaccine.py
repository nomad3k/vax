import pytest
from datetime import date
from vaccine import Vaccine


@pytest.mark.parametrize("interval,a,b,expected", [
    (21, date(2000, 1, 1), date(2000, 1, 21), False),
    (21, date(2000, 1, 1), date(2000, 1, 22), True),
    (21, date(2000, 1, 1), date(2000, 1, 23), True),
    (2, date(2000, 1, 1), date(2000, 1, 2), False),
    (2, date(2000, 1, 1), date(2000, 1, 3), True),
    (2, date(2000, 1, 1), date(2000, 1, 4), True)
])
def test_interval(interval: int, a: date, b: date, expected: bool):
    v = Vaccine(name="test", friendly_name="test") \
        .configure(doses=2, interval=interval)
    actual = v.satisfies_interval(a, b)
    assert actual == expected

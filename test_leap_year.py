# [x] - test divisible_by_4_but_not_100
# [x] - test divisible_by_400
# [x] - test not_divisible_by_4
# [x] - test divisible_by_100_but_not_400

from leap_year import leap_year

def test_divisible_by_4_but_not_100():
    assert leap_year(2024) == True


def test_divisible_by_400():
    assert leap_year(2000) == True


def test_not_divisible_by_4():
    assert leap_year(2023) == False


def test_divisible_by_100_but_not_400():
    assert leap_year(1900) == False
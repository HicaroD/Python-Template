from random import randint
from main import sum


def test_sum():
    first_number = randint(0, 1000)
    second_number = randint(0, 1000)
    assert sum(first_number, second_number) == first_number + second_number

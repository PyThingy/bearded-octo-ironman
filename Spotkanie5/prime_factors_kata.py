"""
This is sample solution of Prime Factors Kata.

This Kata objective is to write a piece of software that will take a natural
number and return a list of it's prime factors.

To run install pytest and execute `py.test prime_factors_kata.py` in the shell
with pytest accessible.
"""

import pytest

def get_prime_factors(number):
    factors = []
    if number != 1:
        divisor = 2
        while divisor<number:
            while (number %divisor==0):
                factors.append(divisor)
                number/=divisor
            divisor+=1
        if number !=1:
            factors.append(number)

    return factors

def test_get_prime_factors_of_one():
	assert get_prime_factors(1) == []

PRIMES ={
    2: [2],
    3: [3],
}
PRIMES_POWER ={
    4: [2,2],
    8: [2,2,2],
    9: [3,3],
    25: [5,5],
    27: [3,3,3],
}

COMPOUNDS = {
    6: [2, 3],
    42: [2, 3, 7],
}

@pytest.mark.parametrize('number, factors', PRIMES.items())
def test_get_prime_factors_of_primes(number, factors):
    assert get_prime_factors(number) == factors

@pytest.mark.parametrize('number, factors', PRIMES_POWER.items())
def test_get_prime_factors_of_primes_power(number, factors):
    assert get_prime_factors(number) == factors

@pytest.mark.parametrize('number, factors', COMPOUNDS.items())
def test_get_prime_factors_of_compund_numbers(number, factors):
    assert get_prime_factors(number) == factors
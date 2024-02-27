from .Practice_ import is_prime
def test_isprime_():
    assert is_prime(6) == False
    assert is_prime(23) == True
    assert is_prime(98) == False
    assert is_prime(8) == False
    assert is_prime(1) == False
    assert is_prime(91) == False


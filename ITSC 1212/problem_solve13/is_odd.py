def is_odd(num: int) -> bool:
    """Returns True if the given number is odd, False otherwise."""
    return num % 2 != 0
# Test cases
print(is_odd(0))     # Expected: False
print(is_odd(11))    # Expected: True
print(is_odd(-19))    # Expected: True
print(is_odd(-20))    # Expected: False

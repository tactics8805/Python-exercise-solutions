def is_divisible(num1, num2):
    """
    Check if num1 is divisible by num2.

    Args:
    num1 (int): The first integer.
    num2 (int): The second integer.

    Returns:
    bool: True if num1 is divisible by num2, False otherwise.
    """
    if num2 == 0:
        raise ValueError("Dividing by zero results in an undefined value.")
    return num1 % num2 == 0
# Test cases
print(is_divisible(10, 2))  # True
print(is_divisible(10, 3))  # False
print(is_divisible(10, 0))  # Raises ValueError

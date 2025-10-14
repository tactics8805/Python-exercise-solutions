# This function evaluates the maximum of two numbers
def max_of_two(a: float, b: float) -> float:
    """
    Returns the maximum of two numbers.

    Parameters:
    a (float): First number.
    b (float): Second number.

    Returns:
    float: The maximum of the two numbers.
    """
    if a > b: 
        return a
    else: 
        return b
# Test cases
print(max_of_two(3, 5))  # Output: 5
print(max_of_two(-1, -5))  # Output: -1
print(max_of_two(2.5, 2.3))  # Output: 2.5

"""Alternative method using built-in function...
def max_of_two(a: float, b: float) -> float:
    return max(a, b)
"""
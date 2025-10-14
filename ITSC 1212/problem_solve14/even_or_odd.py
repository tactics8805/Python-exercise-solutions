# This program will check if a number is even or odd, and then return the result as a string.
def even_or_odd(num: int) -> str:
    '''Returns "Even" if the number is even, "Odd" if the number is odd.
    Args:
        num (int): The number to check.
    Returns:
        str: "Even" or "Odd"
    '''
    if num != int(num):
        raise ValueError("Input must be an integer.")
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Test cases
print(even_or_odd(2))  # Even
print(even_or_odd(3))  # Odd
print(even_or_odd(0))  # Even
print(even_or_odd(-1)) # Odd
print(even_or_odd(-2)) # Even
print(even_or_odd(100)) # Even

def age_checker(a: int) -> bool:
    ''' Checks if the given age is 18 or older.
    Args:
        a (int): The age to check.
    Returns:
        bool: True if age is 18 or older, False otherwise.
    '''
    if a >= 18:
        return True
    else:
        return False
# Test cases
print(age_checker(81))  # Expected output: True
print(age_checker(18))  # Expected output: True
print(age_checker(1))  # Expected output: False
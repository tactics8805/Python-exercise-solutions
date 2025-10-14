def num_checker(num: int) -> str:
    if num >= 0:
        return 1
    else:
        return -1
# Test cases
print(num_checker(50))   # Expected output: 1
print(num_checker(0))  # Expected output: 1
print(num_checker(-3))   # Expected output: -1
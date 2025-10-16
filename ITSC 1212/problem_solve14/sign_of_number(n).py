def sign_of_number(n: float) -> str:
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
# Test cases
print(sign_of_number(10))   # Output: Positive
print(sign_of_number(-5))   # Output: Negative
print(sign_of_number(0))    # Output: Zero
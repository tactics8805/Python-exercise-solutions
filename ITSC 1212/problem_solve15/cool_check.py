def cool_check(word: str, number: int) -> str:
    '''Check if the word is "cool" based on the length of the word and the divisibility of the number.
    
    Arguments:
    word -- the word to check
    number -- the number to check
    
    Returns:
    "cool" if the word is "cool", "less cool" if the word is "less cool", "not cool" otherwise
    A word is considered "cool if its length is greater than 5 and the number is divisible by 2.
    '''
    if len(word) >= 5 and number % 2 == 0:
        return "cool"
    elif len(word) < 5 and number % 2 != 0:
        return "less cool"
    else:
        return "not cool"
# Test cases
print(cool_check("apple",4))      # Expected: "cool"
print(cool_check("hi",7))         # Expected: "less cool" 
print(cool_check("great", 3))     # Expected: "not cool"
print(cool_check("grape", 2))     # Expected: "cool"

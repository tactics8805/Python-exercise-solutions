word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
def length_diff(word1: str, word2: str) -> int:
    # Calculate the absolute difference in length between two words.
    return abs(len(word1) - len(word2))
print("The absolute difference in length is:", length_diff(word1, word2))
# Now, time to run some test cases!
print(length_diff("hello", "world"))  # Expected output: 0
print(length_diff("computer", "science"))     # Expected output: 1
print(length_diff("cat", "elephant"))        # Expected output: 5
print(length_diff("data", "data"))          # Expected output: 0

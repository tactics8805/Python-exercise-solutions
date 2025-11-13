def count_vowels(text: str) -> int:
    """Count the number of vowels in a given text.
    Args:
        text (str): The input text to analyze
        Define the  count_vowels(text:str) so that it:
            Initializes a list of five counters for the vowels a, e, i, o, u, in that order.
            counts = [0,0,0,0,0]
            Iterates through each character of the given text using a for loop.
            Checks if the character is a vowel and increments the matching count.
            After counting is done it prints the results in order.
    Returns:
        int: The number of vowels in the text.
    """
    # Initialize counters for a, e, i, o, u
    counts = [0, 0, 0, 0, 0]
    for char in text:
        if char == 'a':
            counts[0] += 1
        elif char == 'e':
            counts[1] += 1
        elif char == 'i':
            counts[2] += 1
        elif char == 'o':
            counts[3] += 1
        elif char == 'u':
            counts[4] += 1
    # Print the results
    print(f"a: {counts[0]}, e: {counts[1]}, i: {counts[2]}, o: {counts[3]}, u: {counts[4]}")
    print(f"Total vowels: {sum(counts)}")
def main():
    text = input("Enter text: ")
    count_vowels(text)
main()
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
    return counts

def display_histogram(vowels: list[str], counts: list[int]) -> None:
    """Displays a histogram of vowel counts using asterisks.
    
    Args:
        vowels (list[str]): List of vowel characters.
        counts (list[int]): Corresponding counts for each vowel.
    """
    for vowel, count in zip(vowels, counts):
        print(f"{vowel}: {'*' * count}")

def main() -> None:
    """Main function to execute vowel counting and histogram display."""
    text = input("Enter text: ").lower()
    counts = count_vowels(text)
    vowels = ['a', 'e', 'i', 'o', 'u']
    display_histogram(vowels, counts)
main()
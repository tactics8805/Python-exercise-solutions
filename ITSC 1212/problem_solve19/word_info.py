def get_position(sentence: str, position: int) -> str:
    """
    Retrieve the word at the specified position in a sentence.

    Parameters:
    setence (str): The input sentence.
    position (int): The position of the word to retrieve (0-based index).

    Process: 
    1. Split the sentence into words using split method. Assume the words are separated by spaces.
    Returns:
    str: The word at the specified position, or an empty string if the position is out of range.
    """
    words = sentence.split()
    if 0 <= position < len(words):
        return words[position]
    return ""
# Extend analyzing text by counting how many times a particular term or letter appears in a sentence.
def count_term_occurences(sentence: str, term: str) -> str:
    """
    Count how many times a particular term appears in a sentence.

    Parameters:
    sentence (str): The input sentence.
    term (str): The term to count in the sentence.

    Returns:
    int: The number of occurrences of the term in the sentence.
    """
    words = sentence.split()
    if term in sentence:
        return sentence.count(term)
    return 0
def main():
    sentence = input("Enter a sentence: ")
    position = int(input("Enter the position of the word to retrieve (0-based index): "))
    term = input("Enter a word or letter to search for:")
    print(f"Word {position} is: {get_position(sentence, position)}, {len(get_position(sentence, position))} letters, and {term} occurs {count_term_occurences(sentence, term)} time(s).")
main()
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
def main():
    sentence = input("Enter a sentence: ")
    position = int(input("Enter the position of the word to retrieve (0-based index): "))
    print(f"Word {position} is: {get_position(sentence, position)} and it has {len(get_position(sentence, position))} letters.")
main()
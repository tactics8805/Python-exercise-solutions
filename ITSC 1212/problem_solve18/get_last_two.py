def get_last_two(names: list[str]) -> str:
    """
    Returns the last two characters of the given phrase.
    
    Input:
    names[str]: A list of strings.
    
    Returns:
    str: The last two strings of the list as a tuple.
    """
    if len(names) < 2:
        return None
    else:
        return (names[-2], names[-1])
def main():
    print(get_last_two(names = input("Enter a list of names separated by commas: ").split(",")))
main()
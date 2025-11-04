def describe_cheeses(cheeses: list[str]):
    """Prints a description of each cheese in the list.

    inputs:
        cheeses (list[str]): A list of cheese names.
    process:
        print the list's length
        print the third cheese type
        print the second-to-last cheese type
        print all but the last two cheese types
        print the length of the first cheese type

    """
    print(f"Number of cheeses: {len(cheeses)}")
    if len(cheeses) >= 3:
        print(f"Third cheese: {cheeses[2]}")
    if len(cheeses) >= 2:
        print(f"Second-to-last cheese: {cheeses[-2]}")
    if len(cheeses) > 2:
        print(f"All but the last two cheeses: {cheeses[:-2]}")
    if cheeses:
        print(f"Length of the first cheese name: {len(cheeses[0])}")
def main():
    cheese_list = ["Brie", "Cheddar", "Gouda", "Mozzarella", "Parmesan", "Feta"]
    describe_cheeses(cheese_list)
main()
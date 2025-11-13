def print_star_pattern(size: int) -> None:
    """Prints a star pattern of given size. Uses for loops to display the pattern.
    
    Args: 
        size (int): The size of the star pattern.
        After the growing pattern, display a reversed pattern using another for loop.
    """
    # Print the growing pattern
    for i in range(1, size + 1):
        print("*" * i)
    # Print the reversed pattern
    for i in range(0, size):
        print("*" * (size - i))
def main():
    size = int(input("Enter the size of the star pattern: "))
    print_star_pattern(size)
main()


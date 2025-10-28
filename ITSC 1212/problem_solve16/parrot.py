def parrot() -> str:
    '''A simple parrot function that repeats user input until 'quit' is entered.
    Input: None

    Process: Continuously prompt the user for input and repeat it back until 'quit' is entered.

    Output: None

    Variables: user_input - stores the user's input string.

    Example: User says "Hello" -> Output: "Hello"
    '''
    user_input = input("Say something (or 'quit' to stop): ")
    while user_input != "quit":
        if user_input == "":
            print("Please say something!")
            user_input = input("Say something (or 'quit' to stop): ")
        else:
            print(f"{user_input}")
            user_input = input("Say something (or 'quit' to stop): ")
    else:
        print("Goodbye!")

parrot()

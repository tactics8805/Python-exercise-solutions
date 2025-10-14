def full_name(first: str, last: str) -> str:
    """Return a full name string given a first and last name."""
    return str(first) + " " + str(last)
def welcome_message(first: str, last: str) -> str:
    """Return a welcome message given a first and last name."""
    return "Welcome, " + full_name(first, last) + "!"  
# Tests
print(full_name("Ada", "Lovelace"))  # Expected: "Ada Lovelace"
print(welcome_message("Ada", "Lovelace"))  # Expected: "Welcome, Ada Lovelace!"
print(full_name("Alan", "Turing"))  # Expected: "Alan Turing"
print(welcome_message("Alan", "Turing"))  # Expected: "Welcome, Alan Turing!"
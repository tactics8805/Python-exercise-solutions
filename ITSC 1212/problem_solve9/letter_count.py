# Define strings
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
string3 = input("Enter third string: ")
# Establish function to count characters in combination of said strings.
def letter_count(string1, string2, string3):
    return len(string1+string2+string3)
# Output: Total number of letters in the three strings
print(letter_count(string1, string2, string3))

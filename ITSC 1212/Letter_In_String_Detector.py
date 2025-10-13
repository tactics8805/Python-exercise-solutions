# This program checks if a letter is in a word.
# Also making sure to include type annotations so that a fellow programmer knows what type of data to expect.
def letter_in_word(word: str, letter: str) -> bool:
    # We want to check if the letter is in the word. We also want to make sure our program doesn't say True if the user enters an empty string for either the word or the letter.
    if (letter in word and len(word) != 0 and len(letter) != 0): 
        return True
    # Of course, if our conditions aren't met, we want to return False.
    else:
        return False
# Lastly, we want to get input from the user for the word and letter, and print the result of our function.        
print(letter_in_word(word = input("Enter a word: "), letter = input("Enter a letter: ")))
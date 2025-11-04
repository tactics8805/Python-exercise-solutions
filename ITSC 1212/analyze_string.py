def analyze_string(phrase: str):
    string_length = len(phrase)
    third_char_string = phrase[3]
    second_to_last_char_string = phrase[string_length - 2:string_length]
    first_five_char_string = phrase[:5]
    all_char_but_last_two_string = phrase[0:string_length - 2]
    return {string_length, third_char_string, second_to_last_char_string, first_five_char_string, all_char_but_last_two_string}
def main():
    phrase = input("Enter a string at least 5 characters long: ")
    if len(phrase) >= 5:
        print(analyze_string(phrase))
    else: 
        print("Error")
main()
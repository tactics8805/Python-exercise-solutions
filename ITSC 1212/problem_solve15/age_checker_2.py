def age_checker(a: int) -> str:
    '''Check if the age is in age brackets and returns a corresponding message.
    Parameters:
    a (int): The age to check.
    Returns:
    age < 18: "You are a minor."
    age >= 18 and age < 21: "You are an adult."
    age >= 21 and age < 65: "You are 21+."
    age >= 65: "You are a senior citizen."
     '''
    if a < 18:
        return "You are a minor."
    elif 18 <= a < 21:
        return "You are an adult."
    elif 21 <= a < 65:
        return "You are 21+."
    else:
        return "You are a senior citizen."
# Tests
print(age_checker(81))   # Expected: You are a senior citizen.
print(age_checker(18))   # Expected: You are an adult.
print(age_checker(1))    # Expected: You are a minor.
print(age_checker(31))   # Expected: You are 21+.

user_age = int(input("Enter your age: "))
if age_checker(user_age) == "You are a minor.":
    print("Too young to vote!")
elif age_checker(user_age) == "You are an adult.":
    print("You can vote!")
elif age_checker(user_age) == "You are 21+.":
    print("You can drink and vote!")
elif age_checker(user_age) == "You are a senior citizen.":
    print("You can vote, drink, and retire soon!")
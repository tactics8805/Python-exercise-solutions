def dice_roll(num: int) -> str:
    ''' Determines the quality of a dice roll based on the number the dice lands on.
    Parameters:
    num (int): The number the dice lands on (1-6).
    
    Returns:
    if num is in the set {1, 2, 3};  return "Low Roll"
    elif num is in the set {4, 5};  return "High Roll"
    elif num is 6;  return "Lucky Roll"
    '''
    if num in {1, 2, 3}:
        return "Low roll"
    elif num in {4, 5}:
        return "High roll"
    elif num == 6:
        return "Lucky roll"
# Tests
print(dice_roll(4))   # Expected: High roll
print(dice_roll(1))   # Expected: Low roll
print(dice_roll(6))   # Expected: Lucky roll

user_num = int(input("Enter the number your die landed on (1-6): "))
if dice_roll(user_num) == "Low roll":
    print("Better luck next time!")
elif dice_roll(user_num) == "High roll":
    print("Nice roll!")
elif dice_roll(user_num) == "Lucky roll":
    print("Jackpot! You rolled a 6!")
import random
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

def play_dice_game() -> str:
    ''' Simulates rolling a dice until a "Lucky roll" is achieved.
    Input: None
    
    Process: Continuously rolls a dice until a 6 is rolled.
    
    Output: Prints the number of rolls taken to achieve a "Lucky roll".
    
    Variables:
    roll (int): The current dice roll.
    count (int): The number of rolls taken.
    '''
    roll = random.randint(1, 6)
    count = 0
    while dice_roll(roll) != "Lucky roll":
        count += 1
        roll = random.randint(1, 6)
    count += 1  # Count the lucky roll
    print(f"You took {count} rolls to get a lucky roll!")
play_dice_game()
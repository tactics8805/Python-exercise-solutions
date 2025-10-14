def tip(amount: float, percent: float) -> float:
    '''
    Input:  amount (float) - pre-tip total
            percent (float) - decimal tip rate (0-1), e.g., 0.15 for 15%
    Process: multiply amount by percent to get tip amount
    Output: tip amount (float)
    '''
    return amount * percent
def total_with_tip(amount: float, percent: float) -> float:
    '''
    Input:  amount (float) - pre-tip total
            percent (float) - decimal tip rate (0-1), e.g., 0.15 for 15%
    Process: calculate tip using tip() function, then add to amount
    Output: total amount (float)
    '''
    return amount + tip(amount, percent)
# Tests
print(tip(50, 0.2))          # Expected: 10.0
print(total_with_tip(50, 0.2))  # Expected: 60.0
print(total_with_tip(80, 0.15)) # Expected: 92.0

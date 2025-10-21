def weekly_pay(hours_worked: float, hourly_rate: float) -> float:
    '''Calculate the weekly pay based on hours worked and hourly rate.
    
    Arguments:
    hours_worked -- the number of hours worked in a week
    hourly_rate -- the hourly pay rate

    Returns:
    The total weekly pay as a float.
    '''
    if hours_worked <= 40:
        return float(hours_worked * hourly_rate)
    else:
        overtime_hours = hours_worked - 40
        return float((40 * hourly_rate) + (overtime_hours * hourly_rate * 1.5))
# Test cases
print(weekly_pay(35, 20)) # Expected output: 700.0
print(weekly_pay(40, 15))   # Expected: 600.0
print(weekly_pay(45, 10))   # Expected: 475.0
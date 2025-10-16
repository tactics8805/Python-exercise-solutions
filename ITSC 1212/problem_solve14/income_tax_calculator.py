income = float(input("Enter your income: "))
standard_deduction = 15000 # Standard deduction for single filers in 2025 is $15,000
def calculate_income_tax(taxable_income: float) -> float:
    """
    Calculate the income tax based on the given income.
    Tax rates are based on the 2025 U.S. federal income tax brackets for single filers. Tax brackets
    are based on taxable income (income - the standard deduction for that year), are progressive, and are subject to change by inflation adjustments annually.
    Tax brackets:
    - 35% for incomes over $250,525 ($501,050 for married couples filing jointly).
    - 32% for incomes over $197,300 ($394,600 for married couples filing jointly).
    - 24% for incomes over $103,350 ($206,700 for married couples filing jointly).
    - 22% for incomes over $48,475 ($96,950 for married couples filing jointly).
    - 12% for incomes over $11,925 ($23,850 for married couples filing jointly).
    - 10% for incomes $11,925 or less ($23,850 or less for married couples filing jointly).

    Args:
        income (float): The total income.
        taxable_income (float): The taxable income after deductions.

    Returns:
        float: The calculated income tax.
    """
    taxable_income = income - standard_deduction
    if taxable_income <= 0:
        tax = 0  
    # For single taxpayers and married individuals filing separately for tax year 2025, the standard deduction rises to $15,000 for 2025
    if taxable_income <= 11925:
        tax = 0.10 * taxable_income
    elif taxable_income <= 48475:
        tax = (taxable_income - 11925) * 0.22 + (11925 * 0.10)
    elif taxable_income <= 103350:
        tax = (taxable_income - 48475) * 0.24 + (36550 * 0.22) + (11925 * 0.10)
    elif taxable_income <= 197300:
        tax = (taxable_income - 103350) * 0.32 + (54875 * 0.24) + (36550 * 0.22) + (11925 * 0.10)
    elif taxable_income <= 250525:
        tax = (taxable_income - 197300) * 0.35 + (93950 * 0.32) + (54875 * 0.24) + (36550 * 0.22) + (11925 * 0.10)

    return tax
tax = calculate_income_tax(income)
print(f"The income tax on an income of ${income} is ${tax}")
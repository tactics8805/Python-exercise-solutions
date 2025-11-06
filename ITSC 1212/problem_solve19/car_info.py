def get_car_info(makes: list[str], years: list[int], prices: list[int], choice: int) -> str:
    """
    Display information about a list of cars based on functions and indexing.
    Input: 
        makes - list of car makes
        years - list of car years
        prices - list of car prices
        choice - index of the car to display information for
    Process:
        Based on the choice index, retrieve the corresponding make, year, and price from the lists and display them.
    Output:
        A formatted string containing the car's make, year, and price.
    """
    while choice < 1 or choice > 8:
        choice = int(input("Invalid choice. Please enter a number between 1 and 8: "))
    return f"Car Information: {makes[choice-1]}, {years[choice-1]}, {prices[choice-1]}"

def main():
    # car details
    makes = ['Maserati', 'Honda', 'Subaru', 'Fiat', 'Ford', 'Porsche', 'Mazda', 'Lotus']
    years = [2004, 1989, 2002, 2016, 2008, 1989, 2023, 2011]
    prices = [18000, 2499, 6000, 8495, 15499, 33250, 34999, 63915]
    # retrieve car information based on choice index
    choice = int(input("Enter the index of the car you want information about (1-8): "))
    print(get_car_info(makes, years, prices, choice))
main()

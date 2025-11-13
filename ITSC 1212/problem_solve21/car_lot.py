def display_all_cars(makes: list[str], years: list[int], prices: list[float]) -> None:
    """Display all cars in the lot with their details.

    Args:
        Takes three lists (makes, years, and prices)
        You can assume that each car’s information is stored at the same index across the three lists.

        Uses a while loop to traverse the lists.

        On each iteration, prints a formatted line like:

            $18000: A Maserati made in 2004.

        Keeps a running total of all car prices and displays the final total after the loop ends.
    """
    total_price = 0.0
    i = 0
    while i < len(makes):
        print(f"${prices[i]}: A {makes[i]} made in {years[i]}.")
        total_price += prices[i]
        i += 1
    print("-------------------------------------------")
    print(f"The total price of all the cars: ${total_price}")

def main() -> None:
    """Main function to display car lot information.
    """
    makes  = ['Maserati', 'Honda', 'Subaru', 'Fiat', 'Ford', 'Porsche', 'Mazda', 'Lotus']
    years  = [2004, 1989, 2002, 2016, 2008, 1989, 2023, 2011]
    prices = [18000, 2499, 6000, 8495, 15499, 33250, 34999, 63915]
    display_all_cars(makes, years, prices)
main()

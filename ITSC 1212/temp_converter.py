celsius = float(input("Enter temperature in Celsius: "))
def c_to_f(celsius: float) -> float:
    # Convert Celsius to Fahrenheit.
    return (celsius * 9/5) + 32
fahrenheit = c_to_f(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")
# We will now make an algorithm to calculate weighted averages. This is useful in ML, and statistics (probability distributions).
a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))
w1 = float(input("Enter the weight for the first value: "))
w2 = float(input("Enter the weight for the second value: "))
# We will now define a function to calculate the weighted average.
# The formula for weighted average is (a*w1 + b*w2) / (w1 + w2)
def weighted_average(a, b, w1, w2):
    return (a * w1 + b * w2) / (w1 + w2)
# We now need to define a variable to store the result of the function call. Then we will print the result.
weighted_average = weighted_average(a, b, w1, w2)
print(f"The weighted average is: {weighted_average}")
# Now we need to run some test cases to ensure our function works correctly.
# Test case 1: a = 3, b = 5, w1 = 2, w2 = 3
print(weighted_average(3, 5, 2, 3)) # Expected output: 4.2
#Test case 2: a = 10, b = 20, w1 = 1, w2 = 1
print(weighted_average(10, 20, 1, 1)) # Expected output: 15.0
# Test case 3: a = 0, b = 100, w1 = 0.5, w2 = 0.5
print(weighted_average(0, 100, 0.5, 0.5)) # Expected output: 50.0
# Test case 4: a = -10, b = 10, w1 = 1, w2 = 1
print(weighted_average(-10, 10, 1, 1)) # Expected output: 0.0

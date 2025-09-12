age = int(input("Enter your age: "))
if age < 18 and age > 0:
    print("You are a minor, you are not an adult.")
elif age >= 18:
    print("You are an adult.")
else:
    print("You are trolling me. There is no way you are this age and able to interact with this program.")

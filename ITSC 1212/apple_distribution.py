num_apples = int(input("Enter the number of apples: "))
num_teachers = int(input("Enter the number of teachers: "))
if num_teachers == 0:
    print("No teachers to distribute apples to.")
if num_apples < 0 or num_teachers < 0:
    print("Number of apples and teachers must be non-negative.")
if num_apples == 0:
    print("No apples to distribute to teachers.")
if num_teachers > 0 and num_apples >= 0:
    apples_per_teacher = num_apples // num_teachers
    apple_remainder = num_apples % num_teachers
    print("Distribute", apples_per_teacher, "apples to each teacher. You will have ", apple_remainder, "apples left in the basket.")


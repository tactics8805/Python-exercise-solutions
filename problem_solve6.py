userRating = int(input("Enter a value from 1-5. Enter 0 to stop rating."))
total = 0
count = 0
while userRating != 0:
    if 1 <= userRating <= 5:
        total += userRating
        count += 1
    else:
        print("Invalid rating. Please enter a value from 1-5 or 0 to stop.")
    userRating = int(input("Enter a value from 1-5. Enter 0 to stop rating."))
average = total / count if count > 0 else 0
print("Total ratings:", total)
print("Number of ratings:", count)
print("Average rating:", average)
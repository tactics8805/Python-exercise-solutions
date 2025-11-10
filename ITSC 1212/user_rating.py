# this version does not use loops.
great_counter = 0
good_counter  = 0
okay_counter = 0
bad_counter = 0
nums = great_counter + good_counter + okay_counter + bad_counter
while nums < 4:
    print("How are you feeling today? (user 1)")
    print("    4 - Great")
    print("    3 - Good")
    print("    2 - Okay")
    print("    1 - Bad")
    user_input = int(input("-------------------\n"))
    if user_input == 4:
        great_counter += 1
    elif user_input == 3: 
        good_counter += 1
    elif user_input == 2:
        okay_counter += 1
    elif user_input == 1:
        bad_counter += 1
    nums = great_counter + good_counter + okay_counter + bad_counter
# calculate average using scale 4->great , 3 -->good, 2-->okay, 1-->bad
average = ((great_counter  * 4)+ (good_counter  * 3)+ (okay_counter * 2) + (bad_counter * 1)) / 5

print("Average Rating:", average)

print("Ratings Breakdown:")
print("    Bad:", bad_counter)
print("    Okay:", okay_counter)
print("    Good:", good_counter)
print("    Great:", great_counter)

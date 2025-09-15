# First, we need to define a goal for daily steps.
# A common recommendation is to aim for 10,000 steps per day, but for this example, let's set a more achievable goal of 5,000 steps.
# I know that I'm not averaging 10,000 steps a day, so I think 5000 steps is a more reasonable goal.
dailySteps_goal = 5000
# Now we have to get the user's input so that we can compare their daily steps to the goal.
# We will use the input() function to get the user's input and convert it to an integer, since you can't walk a fraction of a step.
# We will also add some error handling to ensure that the user enters a valid number of steps.
dailySteps = int(input("Enter your daily steps: "))
if dailySteps < 0:
        print("Invalid input. Steps cannot be negative.")
elif dailySteps == 0:
        print("No steps taken today.")
elif dailySteps < dailySteps_goal:
    print("You need to walk more.")
# Normal range for meeting and exceeding the goal will be between 5000 and 10000 steps. Recall the 2*z-score rule in statistics.
# If the median is 5000 steps and the standard deviation is 2500 steps, then 95% of the data lies between 0 and 10000 steps.
# Since we only want to reward the users who meet or exceed the goal, we can set the upper limit for the "normal reward" to 10000 steps.
# Any steps above 10000 will be considered as "extraordinary" and will be rewarded with a special message!
elif dailySteps_goal <= dailySteps < 2 * dailySteps_goal:
    print("Good job! Keep going.")
else:
    print("You monster, are you the next David Goggins?")
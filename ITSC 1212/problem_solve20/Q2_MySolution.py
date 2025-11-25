'''
Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7.
What is returned is a list of all of the numbers up until it reaches 7.
'''
def check_nums(nums: list[int]) -> list[int]:
    i = 0
    new_list = []
    while i < len(nums) and nums[i] != 7:
        new_list.append(nums[i])
        i += 1
    return new_list

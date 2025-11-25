'''
Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list.
The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
 '''
def sublist(nums: list[int]) -> list[int]:
    i = 0   
    new_list = []
    while i < len(nums) and nums[i] != 5:
        new_list.append(nums[i])
        i += 1
    return new_list

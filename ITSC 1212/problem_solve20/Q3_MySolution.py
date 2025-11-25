'''
Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list.
The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
'''
def sublist(strings: list[str]) -> list[str]:
    i = 0
    new_list = []
    while i < len(strings) and strings[i] != "STOP":
        new_list.append(strings[i])
        i += 1
    return new_list

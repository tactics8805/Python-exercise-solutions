'''
Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. 
What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops
(i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.). 
If you want to make this even more of a challenge, do this without slicing.
'''
def beginning(user_list: list[str]) -> list:
    i = 0
    new_list = []
    while user_list[i] != "bye":
        new_list.append(user_list[i])
        i += 1
    if len(new_list) <= 10:
        return new_list
    else:
        return new_list[0:10]

def count_up(limit):
    """Counts from 1 to the specified limit and returns a list of numbers.
    Lists have not been taught yet, unfortunately, so we have to use a while loop.
    
    Input: an integer limit
    Process: counts from 1 to limit
    Output: a list of integers from 1 to limit
    """
    if limit < 1:
        raise ValueError("Limit must be at least 1.")
    else:
        count = 1
        while limit >= count:
            print(count)
            count += 1
        print("Done!")

# Example run
count_up(4) # This will print numbers from 1 to 4 and then "Done!"

            
    
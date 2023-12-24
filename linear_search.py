def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    
    for i in range(len(list)):
        if list[i] == target:
            return i 
    return None

    """
    OR
    """
    
    for i, item in enumerate(list):
        if item == target:
            return i
    return None 


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")
        

numbers = [i for i in range(1,11)]

result = linear_search(numbers, 6)
verify(result)
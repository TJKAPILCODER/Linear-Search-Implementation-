def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns  O(N)
    """
    for i in range(0, len(list)):
        if(list[i] == target):
            return i
    return None
# VERIFY RETURN 
def verify(index):
    if index is not None:
        print("Target found at index ", index)
    else:
        print("Target not found in list")
# TEST
result = linear_search([1,2,3,4,5], 4)
verify(result)

result = linear_search([1,2,3,4,5], 7)
verify(result)

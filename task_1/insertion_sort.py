def insertion_sort(lst) -> list:
    """
    Sorts a list using the Insertion Sort algorithm.

    Time Complexity:
        - Best: O(n) when the list is already sorted.
        - Average and Worst: O(n^2) for unsorted lists.
    
    Parameters:
        lst (list): The list of elements to be sorted.

    Returns:
        list: A sorted list of elements in ascending order.
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst
def merge_sort(arr) -> list:
    """
    Sorts a list using the Merge Sort algorithm.

    Time Complexity:
        - Best, Average, and Worst: O(n log n) in all cases.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A sorted list of elements in ascending order.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right) -> list:
    """
    Merges two sorted lists into a single sorted list.

    Time Complexity: O(n), where n is the total number of elements in both lists.

    Parameters:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: A merged sorted list combining elements from both input lists.
    """
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged
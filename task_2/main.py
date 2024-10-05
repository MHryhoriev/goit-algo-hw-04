from merge_sort import merge_sort
from itertools import chain

def merge_k_lists(lists):
    """
    Merges k sorted lists into a single sorted list.

    Parameters:
        lists (list of list): A list containing k sorted lists.

    Returns:
        list: A single sorted list containing all the elements from the input lists.
    """
    return merge_sort(list(chain.from_iterable(lists)))

def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)

if __name__ == "__main__":
    main()
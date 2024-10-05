import timeit
import random
from merge_sort import merge_sort
from insertion_sort import insertion_sort

def main():
    sizes = [100, 1000, 10000]

    for size in sizes:
        print(f"\nAnalyzing sorting algorithms for dataset of size: {size}")

        test_data = [random.randint(0, 1000) for _ in range(size)]

        # Test merge_sort
        merge_sort_execution_time = timeit.timeit(lambda: merge_sort(test_data.copy()), number=10)
        print(f"Execution time for Merge sort: {merge_sort_execution_time:.6f} seconds")

        # Test insertion_sort
        insertion_sort_execution_time = timeit.timeit(lambda: insertion_sort(test_data.copy()), number=10)
        print(f"Execution time for Insertion sort: {insertion_sort_execution_time:.6f} seconds")

        # Test Python's built-in sort (Timsort)
        timsort_execution_time = timeit.timeit(lambda: test_data.copy().sort(), number=10)
        print(f"Execution time for Timsort sort: {timsort_execution_time:.6f} seconds")

if __name__ == "__main__":
    main()
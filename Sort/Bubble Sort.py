# Bubble Sort in Python using a function
def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(n - i - 1):

            # Compare adjacent elements
            if array[j] > array[j + 1]:
                # Swap elements
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


array = [64, 34, 25, 12, 22, 11, 90, 5]

sorted_array = bubble_sort(array)

print("Sorted Array:", sorted_array)

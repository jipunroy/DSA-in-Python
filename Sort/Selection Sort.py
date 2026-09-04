# Selection Sort using a function

def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        # Swap
        array[i], array[min_index] = array[min_index], array[i]

    return array


array = [7, 12, 9, 11, 3]

print("Before sorting:", array)

selection_sort(array)

print("After sorting:", array)
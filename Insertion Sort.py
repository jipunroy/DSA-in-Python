#Insertion Sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

array = [7, 12, 9, 11, 3]
print("Before sorting:", array)
insertion_sort(array)
print("After sorting:", array)

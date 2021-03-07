# Insertion Sort Algorithm

# for j = 1 to A.length
def insertion_sort(array):
    for right in range(1, len(array)):

        key = array[right]

        # insert array[right] into the sorted sequence array[0...right-1]
        left = right - 1
        while left > 0 and array[left] > key:
            array[left + 1] = array[left]
            left -= 1
        array[left + 1] = key
    return array


a = [8, 5, 2, 9, 5, 6, 3]
print(f"The unsorted array is {a}")

print(f"The sorted array is {insertion_sort(a)}")

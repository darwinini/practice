
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j-=1

    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]





a = [1, 5, 6, 4, 3, 2]

print(f"The unsorted array is {a}")

print(f"The sorted array is {insertion_sort(a)}")

# a = "Annaliese"
# print(f"My name is: {a}")


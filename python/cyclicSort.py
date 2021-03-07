# Algorithm to sort a cylic array

def cyclicSort(nums):
    # a tracker/counter
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            swap(i, j, nums)
        else:
            i +=1
    return nums

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


def main():
    array = [8, 3, 5, 7, 4, 6, 2, 1]
    print(f"The unsorted array is: {array}")
    print(f"The sorted array using cyclic sort is: {cyclicSort(array)}")

    # Complexity: O(N) + O(N-1) ~ O(N) Time | O(1) Space

main()
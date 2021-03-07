def isValidSubsequence(array, sequence):
    # Write your code here.
    j = 0

    array.sort()
    sequence.sort()

    length = len(array) -1


    for i in range(length):
        if j < len(sequence) and sequence[j] == array[i]:
            j+=1

    if j == len(sequence) -1:
        return True
    else:
        return False


# array = [5,1,22,25,6,-1,8,10]
# array = [5, 1, 22, 25, 6, -1, 8, 10]
array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10, 8]
# sequence = [22, 25, 6]
# sequence = [1, 6, -1, 10]
sequence = [5, 1, 25, 22, 6, -1, 8, 10]

check = isValidSubsequence(array, sequence)
print(f"the array is {array}")
print(f"the sequence is {sequence}")
print(f"the sequence is a {check} part of the array")






# return indexes of a list if the sum = target sum

def NumberSum(array, sum):
    for i in array:
        j = i + 1
        for j in array:
            if sum == i + j and i != j:
                print(f"The value of i is {i}")
                print(f"The value of j is {j}")
                print(f"The value of sum is {sum}")
                index = (array.index(i), array.index(j))
                return index





# array = [3, 5, -4, 8, 11, 1, -1, 6]
array = [14]

target = 15
print(f"The array is {array}")
print(f"The indexes which sum to {target} are {NumberSum(array, target)}")



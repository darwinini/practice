# need algorithm that traverses the array twice

# store every number in a hash table

# array = [3, 5, -4, 8, 11, 1, -1, 6]

# targetSum = 10

# currentNum = x

# need find: x + y = 10

def NumberSum(array, sum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == sum:
                return [array.index(firstNum), array.index(secondNum)]


    return []

# array = [3, 5, -4, 8, 11, 1, -1, 6]
array = [3, 2, 4, 1, 4]
target = 6

print(f"The indexes when target is {target} is {NumberSum(array, 10)}")

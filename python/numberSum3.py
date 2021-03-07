def NumberSum(list, targetSum):
    left = 0
    right = len(list) - 1

    while left < right:

        guess = list[left] + list[right]

        if guess < targetSum:
            left +=1
        elif guess > targetSum:
            right -=1

        else:
            return [left, right]

        print(f"the new value of low is {list[left]}")
        print(f"the new value of high is {list[right]}")

    return []


array = [3,2,4]
array.sort()
print(f"The new sorted array is: {array}")
# array = [2, 2, 2, 1, 1, 5, -4, 11, 1, -1]

target = 6

print(f"The indexes of two numbers that add up to {target} are {NumberSum(array, target)}")



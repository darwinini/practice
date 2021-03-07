# need algorithm that traverses the array twice

# store every number in a hash table

# array = [3, 5, -4, 8, 11, 1, -1, 6]

# targetSum = 10

# currentNum = x

# need find: x + y = 10
# such that y = 10 - x

def twoNumberSum(array, targetSum):
    nums = {}

    for num in array:
        potentialMatch = targetSum - num
        print(f"The current number is now: {num}")
        print(f"The potential_target is now: {potentialMatch}")
        if potentialMatch == targetSum:
            return [potentialMatch, num]
        else:
            nums[num] = True
            print(f"the hash table contains: {nums}")
    return []

array = [3, 5, -4, 8, 11, 1, -1, 6]

target = 10

print(f"The target is {target}")
print(f"The result is {twoNumberSum(array, target)}")


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for num in nums:
            potentialMatch = target - num
            if target == potentialMatch:
                index = [nums.index(num), nums.index(potentialMatch)]
                return index
            else:
                hash[num] = True
        return None



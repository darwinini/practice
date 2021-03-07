# This program returns the greater sum of an array with window size k

def maxSum(K, arr):
    maximum, windowSum, windowStart = 0.0, 0.0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= K - 1:
            # print(f"The max at index {windowEnd} is {maximum}")
            maximum = max(maximum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1



    return maximum


array = [2, 1, 5, 1, 3, 2]
result = maxSum(3, array)
print(result)




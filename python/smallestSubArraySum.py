import math

def smallestSub(s, arr):

    windowSum, windowStart = 0.0, 0
    #choose a very large length that eventually shrinks
    min_length = math.inf

    for windowEnd in range(0, len(arr)):
        # First, we will add-up elements from the beginning of the array until their sum becomes greater than or equal to ‘S.’
        # These elements will constitute our sliding window. We are asked to find the smallest such window having a sum greater than or equal to ‘S.’ We will remember the length of this window as the smallest window so far.
        # After this, we will keep adding one element in the sliding window (i.e., slide the window ahead) in a stepwise fashion.
        windowSum += arr[windowEnd]

        while windowSum >= s:
            # Check if the current window length is the smallest so far, and if so, remember its length.
            min_length = min(min_length, windowEnd - windowStart + 1 )
            # We will shrink the window until the window’s sum is smaller than ‘S’ again. This is needed as we intend to find the smallest window.
            # Subtract the first element of the window from the running sum to shrink the sliding window.
            windowSum -= arr[windowStart]
            windowStart += 1
    # if the window never shrinks, then there is no sum greater than or equal to s
    if min_length == math.inf:
        return 0
    return min_length

def main():
    A = [2, 1, 5, 2, 8]
    S = 7
    print(f"input array is {A}")
    print(f"the result is {smallestSub(S, A)}")


main()


# Find the smallest sub-array length of a given sum

# Array = [2, 1, 5, 5, 2, 8]
# S = 7
# declare a window_sum, smallest_length, window_start
# use a window_sum to reach up to the given sum of S = 7
#  iterate over the range (0, len(array))
# when the window_sum reaches 7 or greater:
    # update the smallest lenght to be the least that gets compared between smallest_length and window_sum
    # subtract the element at window_start from the window_sum
    # increment the window_start
# if smallest_length is equal to infinity, then return -1

def smallestSubFunction(array, sum):
    smallest_length = math.inf
    window_start = 0
    window_sum = 0
    for window_end in range(0, len(array)):
        window_sum += array[window_end]

        while window_sum >= sum:
            # incorrect: smallest_sum = min(smallest_sum, window_sum)
            # need to compare smallest_length with: (window_end - window_start) +1
            smallest_length = min(smallest_length, window_end - window_start + 1)
            window_sum -= array[window_end]
            window_start += 1
    if smallest_length == math.inf:
        return -1

    return smallest_length

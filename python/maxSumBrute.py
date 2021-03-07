def max_sub_array_of_size_k(k, arr):
  max_sum = 0
  window_sum = 0

  for i in range(len(arr) - k + 1):
    window_sum = 0
    for j in range(i, i+k):
      window_sum += arr[j]
    max_sum = max(max_sum, window_sum)
  return max_sum


def main():
    k = 3
    array = [2, 1, 5, 1, 3, 2]
    # print(f"max sum when size is {k} is {maxSum(k,array)}")
    print(max_sub_array_of_size_k(k,array))


main()
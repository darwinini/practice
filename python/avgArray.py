# Program to find the average of all contiguous subarrays of size ‘5’ in the given array

def avg(k, array):
    avg_array = []

    for i in range(0, len(array) - k + 1):
        sub = array[i:i+k]
        sum, avg = 0, 0
        # print(f"The subarray is {sub}")
        for j in sub:
            sum+= j
        avg = sum / 5
        avg_array.append(avg)
    return avg_array

def main():
    # test our avg function
    k = 5
    a = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print(f"The input array is {a}, with k = {k}")
    print(f"The averaged array is {avg(k,a)}")
    print(f"the complexity for this algorithm is O(N*K) time | O(N) Space")


main()

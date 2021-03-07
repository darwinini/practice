# This program will remove any duplicates from a sorted array

# have two pointers that initially point to the same index
# start iterating through the array:
    # compare the next element to the initial element to see if they are equal, if they are:
        # hold the position of the unequal element
        # remove the second element from the array (hopefully array re-sizes and subsequent elements fall into place
        # continue removing until next unique element is found
        # When unique element is found, increase position of initial element
        # return the length of the resulting array




def main():

    array = [3, 2, 3, 6, 3, 10, 9, 3]

    print(f"the input array is: {array}")
    print(f"the resulting array is: {removeDuplicates(array)}")
    print(f"the length of the resulting array is {len(removeDuplicates(array))}")

main()
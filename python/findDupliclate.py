# find the duplicate in a list

def findDuplicate(nums):
    i = 0

    while i < len(nums):
      # check that current element != adjacent element before setting j
      if nums[i] != i + i:
          # j is the correct index for the first number
          j = nums[i] - 1
          if nums[i] != nums[j]:
              swap(i, j, nums)
          else:
              return nums[i]
      else:
          i += 1
    # if nothing found
    return -1


def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]

def main():
    array = [8, 3, 5, 7, 4, 6, 2, 3]
    print(f"the duplicate number is: {findDuplicate(array)}")

main()
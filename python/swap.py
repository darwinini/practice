#step 1 - declare the variables
tempVal = 0



def swap(val1, val2):
    array = [val1, val2]

    list(array)
    array[0], array[1] = array[1], array[0]
    print(f"array[0] is {array[0]}")
    print(f"array[1] is {array[1]}")


swap(2,3)





# print(f"The value of tempVal is {tempVal}")
# print(f"The value of val1 is {val1}")
# print(f"the Value of val2 is {val2}")
#
# tempVal = val1
# print("tempVal = val1")
# print(f"The value of tempVal is {tempVal}")
# val1 = val2
# print("val1 = val2")
# print(f"The value of val1 is {val1}")
# print("val2 = tempVal")
# val2 = tempVal
# print(f"the Value of val2 is {val2}")

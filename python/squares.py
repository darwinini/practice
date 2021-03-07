from functions import square
# To import the entire module from the file functions
# import functions

# To just import the function square from the functions module
# from functions import square

for i in range(10):
    # when importing the entire module
    # print(f"The square of {i} is {functions.square(i)}")

    # when just importing the square module
    print(f"The square of i {i} is {square(i)}")
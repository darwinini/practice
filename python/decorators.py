# Decorators

# functional programming paradigm, a function that modifies another function
# just as there are ways to take a number and modifying that number,
# there are ways in python to take a function and modifying that function
# and adding additional behavior to that function
# takes a function as input, and returns a modified function
# decorator
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("done with the function")
    return wrapper

# Add the announce decorator to the hello function
@announce
def hello():
    print("Thank, Lord!")

hello()


# Classes are a template for a type of object


class Point():
    # define what a point is
    # automatically be called everytime I try to create a point
    # every function that
    # __init__ is a function that will be called everytime I try to create a new point
    # All functions that operation on objects themselves (aka method), will take the first argument self

    def __init__(self, input_x, input_y):
        # What do we need to store all these data inside of that point
        # when I create
        # need to store the data inside of the self
        self.x = input_x
        self.y = input_y

p = Point(2,8)

print(p.x)
print(p.y)
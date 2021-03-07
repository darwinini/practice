list = [1,2,3,4,5]

i = 0

x = 0

#round 1: x = 1
#round 2: x = 1 + 2 = 3
#rounmd 3: x = 3 + 3 = 6

while i < 5:
    x = x + list[i]
    print(f"The value of x at {i}th step is {x}")
    i = i + 1

x = x/5
print(f"The final value of x is {x}")





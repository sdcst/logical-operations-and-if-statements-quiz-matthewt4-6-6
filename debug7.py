#!python3
"""
Debug this program so that it runs correctly

original code
x = 3
y = 7
z = 9

if x < y > z:
    print("the middle number is ", y)
else:
    print("the middle number is not",y)
"""

x = input("enter in 1st number")
x = float(x)

y = input("enter in 2nd number")
y = float(y)

z = input("enter in 3rd number")
z = float(z)

if y > x and y < z:
    print("the middle number is ", y)
else:
    print("the middle number is not",y)
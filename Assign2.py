"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

x = input("enter in 1st number ")
x = float(x)

y = input("enter in 2nd number ")
y = float(y)

z = (x**2 + y**2)

answer = input("which variable do you want to be the hypotenuse, answer with 'neither' if neither will be the hypotenuse ")

if answer == 'neither':
    print(f"{z} is your missing value")

if answer == "x":
    z = x
    x = (z**2 + y**2)
    print(f"{x} is your missing value")


if answer == "y":
    z = y
    y = z
    print(f"{y} is your missing value")



    
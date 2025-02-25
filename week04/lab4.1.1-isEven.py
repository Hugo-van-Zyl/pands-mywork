'''
Write a program (isEven.py) that asks the user to enter in a number, and the
program will tell the user if the number is even or odd.

'''
#author - Hugo van Zyl

input_nr = int(input("Enter a valid integer - "))

if (input_nr % 2) == 0:
    print("input is an even number")
else:
    print("input is an odd number")
#Write a program called convert.py that takes in a float amount of dollars and returns that absolute amount in cent.
import math
number = float(input("Please enter an amount"))
absoluteValue = abs(number)*100
print(f"{absoluteValue:.0f}")
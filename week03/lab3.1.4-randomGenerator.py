# program that prints out a random number between 1 and 10
import random
range_start = int(input("Enter the start of the range : "))
range_end = int(input("Enter the end of the range : "))
number = random.randint(range_start,range_end)
print("here is a random number {}".format(number))
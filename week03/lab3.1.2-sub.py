# Program to subtract on number from another.
# input reads in a string so we need to convert it into an int

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
answer= a-b
print("{} minus {} is {} ".format(a, b, answer))

#entering in someting other than a number like hello causes an error
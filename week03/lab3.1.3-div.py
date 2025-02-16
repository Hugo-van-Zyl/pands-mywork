# program that reads in two numbers and
# outputs the integer answer and remainder
a = int(input("Enter first number: "))
b = int(input("Enter the number you want to divide by: "))
answer = int(a//b) # // gives the int division
remainder = a%b # % gives the remainder
print("{} divided by {} is {} with remainder {}".format( a, b, answer, remainder))
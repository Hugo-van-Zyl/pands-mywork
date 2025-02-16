# nameAndAge.py
# This program displays user input for name and age with some formatting
# author: Hugo van Zyl

name = input("What is your name? ")
age = input("What is your age? ")

#print output without tab before your age
print("Hello ",name, ", your age is ",age,".", sep="")
#print output with tab before your age
print("Hello ",name, ",\t your age is ",age,".", sep="")
'''
Write a program (isEven.py) that as
program will tell the user if the n

Extra - How would you use a while loop to modify 1 so that it keeps prompting the
user for a number until the user enters -1


'''
#author - Hugo van Zyl

while True:
    input_nr = int(input("Enter a valid integer - "))

    if input_nr == -1:
        print(input_nr)
        break
    else:
        print("Try again")
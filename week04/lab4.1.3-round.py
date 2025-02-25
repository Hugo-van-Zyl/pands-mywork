'''
Write a program (grade.py) that rea
prints out corresponding the grade 
percentage is valid:
• Under 40% => Fail
• Between 40% and 49% => Pass
• Between 50% and 59% => Merit 2
• Between 60% and 69% => Merit 1
• Over 70% => Distinction

Extra - In practice the percentages are rounded ie 69.5 gets rounded to 70 so is
equal to a Distinction.
How would you modify the program in 1 to deal with this?
I see two ways.

'''
#author - Hugo van Zyl

input_percent1 = float(input("Enter your module mark (between 0 and 100) - "))
input_percent = round(input_percent1,0)
print(input_percent)

if (input_percent >= 70):
    print("Distinction")
elif (input_percent >= 60):
    print("Merit 1")
elif (input_percent >= 50):
    print("Merit 2")
elif (input_percent >= 40):
    print("Pass")
else:
    print("input is an odd number")
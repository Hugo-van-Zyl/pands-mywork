'''
Write a program (grade.py) that reads in a student’s percentage mark and
prints out corresponding the grade (the program should check that the
percentage is valid:
• Under 40% => Fail
• Between 40% and 49% => Pass
• Between 50% and 59% => Merit 2
• Between 60% and 69% => Merit 1
• Over 70% => Distinction
'''
#author - Hugo van Zyl

input_percent = float(input("Enter your module mark (between 0 and 100) - "))

if (input_percent > 70):
    print("Distinction")
elif (input_percent >= 60):
    print("Merit 1")
elif (input_percent >= 50):
    print("Merit 2")
elif (input_percent >= 40):
    print("Pass")
else:
    print("input is an odd number")
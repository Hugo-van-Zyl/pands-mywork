# Define function to get multiple students' info from user

students = []

while True:
    student = {}
    student["name"] = input("Enter student name (or press Enter to finish): ")
    if student["name"] == "":
        break
    
    student["courses"] = {}
    
    # Read in module names and grades
    while True:
        course = input("Enter course name (or press Enter to finish): ")
        if course == "":
            break
        
        grade = input(f"Enter grade for {course}: ")
        student["courses"][course] = grade
    
    students.append(student)

# Print all students' data
for student in students:
    print("\nStudent Name:", student["name"])
    print("Courses and Grades:")
    for course, grade in student["courses"].items():
        print(f"  {course}: {grade}")


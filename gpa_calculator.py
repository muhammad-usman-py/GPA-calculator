from random import randint
import uuid


class student_gpa:
    # contructor . dunder method
    def __init__(self):
        self.name = input("Please enter your name:\n")
        self.st_id = "STD:"+str(randint(1000, 9999))
        print(f"Hey, {self.name} StudentID assigned to you is {self.st_id}")
        # self.st_id=str(uuid.uuid4())[:8]

        total_points=0
        total_credits=0
        def grade_to_points(grade):
            # Map letter grades to numerical grade points
            maping = {
                'A': 4.0,
                'B': 3.0,
                'C': 2.0,
                'D': 1.0,
                'F': 0.0
            }
            # Return the grade point for the given letter grade (case-insensitive), default to 0 if invalid
            return maping.get(grade.upper(), 0)

        courses = []
        # Ask user how many courses they want to enter
        num_courses = int(input("Enter number of Courses :\n"))

        # Loop through each course to gather credit hours and grade
        for i in range(num_courses):

            # Input credit hours for the current course
            credit_hours = float(input(f"Enter credit hours for course {i+1}:\n"))

            # Input credit hours for the current course
            grade = input(f"Enter grade for course {i+1} (A,B,C,D,F):\n")

            print("-"*40)

            # Append a tuple containing course label, credit hours info, and grade points info
            Grades_points=grade_to_points(grade)
            courses.append((f"course {i+1}", (f"Credit hours:{credit_hours}"), (f"Grades:{Grades_points}")))
            
            # this will calulate neccesaory things for GPA 
            total_points+=(credit_hours*Grades_points)
            total_credits+=credit_hours
            print("-"*40)
            
        self.GPA=total_points/total_credits
        
    def gpa_calculator(self):
        print(f"Name: {self.name}\nSTD_ID: {self.st_id}\nGPA: {self.GPA}")
        
student = student_gpa()
student.gpa_calculator()
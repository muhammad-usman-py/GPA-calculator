# 🎓 Student GPA Calculator

A Python program to calculate a student's GPA based on user-inputted courses, credit hours, and grades. Each student is assigned a random student ID.

---

## ✨ Features

- 👤 Input student name and assign a random student ID.
- 📚 Input multiple courses with credit hours and letter grades.
- 🔢 Converts letter grades (A-F) to grade points.
- 📊 Calculates weighted GPA based on credit hours and grades.
- 🖥️ Displays student info along with calculated GPA.

---

## 🧾 Code Overview

```python
from random import randint
import uuid

class student_gpa:
    # Constructor: gathers student info and course data
    def __init__(self):
        self.name = input("Please enter your name:\n")
        self.st_id = "STD:" + str(randint(1000, 9999))
        print(f"Hey, {self.name} StudentID assigned to you is {self.st_id}")

        total_points = 0
        total_credits = 0
        
        def grade_to_points(grade):
            # Map letter grades to numerical grade points
            mapping = {
                'A': 4.0,
                'B': 3.0,
                'C': 2.0,
                'D': 1.0,
                'F': 0.0
            }
            # Return grade points, default to 0 for invalid grades
            return mapping.get(grade.upper(), 0)

        courses = []
        num_courses = int(input("Enter number of Courses :\n"))

        for i in range(num_courses):
            credit_hours = float(input(f"Enter credit hours for course {i+1}:\n"))
            grade = input(f"Enter grade for course {i+1} (A,B,C,D,F):\n")

            print("-" * 40)

            grade_points = grade_to_points(grade)
            courses.append((f"course {i+1}", f"Credit hours: {credit_hours}", f"Grades: {grade_points}"))

            total_points += credit_hours * grade_points
            total_credits += credit_hours

            print("-" * 40)

        self.GPA = total_points / total_credits

    def gpa_calculator(self):
        print(f"Name: {self.name}\nSTD_ID: {self.st_id}\nGPA: {self.GPA}")

student = student_gpa()
student.gpa_calculator()
```


## 🚀 Usage

1. ▶️ Run the program.
2. 📝 Enter your name when prompted.
3. 🔢 Input the number of courses you want to calculate GPA for.
4. ⏳ For each course:
   - Enter the credit hours.
   - Enter the letter grade (A, B, C, D, or F).
5. 📈 View your calculated GPA and student ID.

---

## 📝 Notes

- 🎫 Student IDs are randomly assigned in the format `STD:xxxx`.
- 🎓 Grades are converted to grade points using a standard 4.0 scale:
  - A = 4.0, B = 3.0, C = 2.0, D = 1.0, F = 0.0.
- ⚖️ GPA is weighted by the credit hours of each course.
- ❗ Invalid grades default to zero points.
- 💡 Make sure to input valid grades and credit hours to get accurate GPA calculations.

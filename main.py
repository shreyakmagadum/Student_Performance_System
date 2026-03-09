# ============================================================
# Student Performance Analysis System Using Pure Python
# ============================================================

import math

# List to store student objects
students = []

# ============================================================
# Task 1: Student Class
# ============================================================

class Student:

    def __init__(self, student_id, name, branch, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.marks = marks

    # Calculate total marks
    def calculate_total(self):
        return sum(self.marks)

    # Calculate average marks
    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    # Calculate grade based on average
    def calculate_grade(self):

        avg = self.calculate_average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


# ============================================================
# Task 2: Student Management Functions
# ============================================================

def add_student():

    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")

    marks = []

    subjects = ["Maths", "Physics", "Programming", "Electronics", "Signal Processing"]

    for sub in subjects:
        m = float(input(f"Enter marks in {sub}: "))
        marks.append(m)

    s = Student(student_id, name, branch, marks)
    students.append(s)

    print("Student added successfully")


def display_students():

    if len(students) == 0:
        print("No students available")
        return

    for s in students:

        print("\n---------------------------")
        print("ID:", s.student_id)
        print("Name:", s.name)
        print("Branch:", s.branch)
        print("Marks:", s.marks)
        print("Total:", s.calculate_total())
        print("Average:", round(s.calculate_average(), 2))
        print("Grade:", s.calculate_grade())


def search_student():

    sid = input("Enter Student ID to search: ")

    for s in students:

        if s.student_id == sid:

            print("\nStudent Found")
            print("Name:", s.name)
            print("Branch:", s.branch)
            print("Marks:", s.marks)
            return

    print("Student not found")


def find_topper():

    if len(students) == 0:
        print("No students available")
        return

    topper = students[0]

    for s in students:

        if s.calculate_average() > topper.calculate_average():
            topper = s

    print("\nClass Topper")
    print("Name:", topper.name)
    print("Average:", round(topper.calculate_average(),2))


def subject_highest():

    subjects = ["Maths", "Physics", "Programming", "Electronics", "Signal Processing"]

    for i in range(5):

        highest = 0
        topper_name = ""

        for s in students:

            if s.marks[i] > highest:
                highest = s.marks[i]
                topper_name = s.name

        print(subjects[i], "Highest:", highest, "by", topper_name)


def class_average():

    if len(students) == 0:
        print("No students available")
        return

    averages = []

    for s in students:
        averages.append(s.calculate_average())

    avg = sum(averages) / len(averages)

    print("Class Average:", round(avg,2))


# ============================================================
# Task 3: File Handling
# ============================================================

def save_data():

    file = open("students_dataset.csv", "w")

    for s in students:

        line = f"{s.student_id},{s.name},{s.branch}," + ",".join(map(str, s.marks))
        file.write(line + "\n")

    file.close()

    print("Data saved successfully")


def load_data():

    try:

        students.clear()   # avoid duplicate loading

        file = open("students_dataset.csv", "r")

        next(file)  # skip header row

        for line in file:

            data = line.strip().split(",")

            student_id = data[0]
            name = data[1]
            branch = data[2]

            marks = list(map(float, data[3:]))

            s = Student(student_id, name, branch, marks)

            students.append(s)

        file.close()

        print("Data loaded successfully")

    except FileNotFoundError:

        print("File not found")


# ============================================================
# Task 4: Statistical Analysis
# ============================================================

def subject_average():

    if len(students) == 0:
        print("No students available")
        return

    totals = [0]*5

    for s in students:

        for i in range(5):
            totals[i] += s.marks[i]

    print("\nSubject Average Marks")

    for i in range(5):

        avg = totals[i] / len(students)

        print("Subject", i+1, "Average:", round(avg,2))


def standard_deviation():

    marks = []

    for s in students:
        marks.extend(s.marks)

    mean = sum(marks) / len(marks)

    variance = 0

    for m in marks:
        variance += (m - mean) ** 2

    variance = variance / len(marks)

    sd = math.sqrt(variance)

    print("Standard Deviation:", round(sd,2))


def grade_distribution():

    grades = {"A":0,"B":0,"C":0,"D":0,"F":0}

    for s in students:

        g = s.calculate_grade()

        grades[g] += 1

    print("\nGrade Distribution")

    for g in grades:
        print(g, ":", grades[g])


# ============================================================
# Task 5: Menu Driven Interface
# ============================================================

def menu():

    while True:

        print("\n========== Student Performance System ==========")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Find Topper")
        print("5. Subject Highest Marks")
        print("6. Class Average")
        print("7. Subject Average")
        print("8. Standard Deviation")
        print("9. Grade Distribution")
        print("10. Save Data")
        print("11. Load Data")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            find_topper()

        elif choice == "5":
            subject_highest()

        elif choice == "6":
            class_average()

        elif choice == "7":
            subject_average()

        elif choice == "8":
            standard_deviation()

        elif choice == "9":
            grade_distribution()

        elif choice == "10":
            save_data()

        elif choice == "11":
            load_data()

        elif choice == "12":
            print("Exiting Program")
            break

        else:
            print("Invalid choice")


# ============================================================
# Program Execution
# ============================================================

menu()
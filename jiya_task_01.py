"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 01: Variables, Data Types, Input, Operators & Typecasting
==============================================================

 Name     : Jiya Maheshwari

 Save as  : jiya_task_01.py   
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 How to use this file
 --------------------
 1. Write your code below each "# Your code here" line.
 2. Run the file in VS Code and check your output against
    the example output given with each task.
 3. Make sure the whole file runs without errors before
    you upload it.

 Stuck? Share a screenshot of your code and the error in the
 CodeStart discussion group. Mistakes are part of learning.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# The exercise questions are in the Session 01 recording.
# Watch the video, note down Exercises 1, 2 and 3, and solve
# them here.
#
# Session 01 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

# Your code here
print(7/2) # output -> 3.5, divides 7 by 2
print(7 // 2)         # 3 -> floor division (drops decimal part)
print("7" + "2")        # 72 -> concatenates string values rather than adding numbers
print(type(7.0))        # <class 'float'> -> 7.0 is a floating-point number
print(2 + 3 * 4 ** 2)   # 50 -> evaluates ** first (16), then * (48), then + (50)
print(bool("0"))        # True -> non-empty strings cast to True in Python


# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

# Your code here
# Fixed bugs:
# 1. Line 2 (NameError): changed `name` to `Name` to match line 1
# 2. Line 5 (TypeError): cast `age` with `int(...)` before adding 1
# 3. Line 7 (SyntaxError): added missing closing quote `"` on `print("Done")`

Name = input("Name: ")
print("Hello", Name)

age = int(input("Age: "))
print("Next year:", age + 1)

print("Done")


# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

# Your code here
total_bill = int(input("Total bill: "))
num_friends = int(input("Number of friends: "))

print("Each pays:", total_bill // num_friends)
print("Left over:", total_bill % num_friends)

print("Exact share (/):", total_bill / num_friends)


# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Variables and Data Types
#
# Create four variables about yourself:
#   - your name   (string)
#   - your age    (integer)
#   - your height in metres (float)
#   - whether you are a student (boolean)
#
# Print each value along with its data type using type().
# Add at least one comment explaining your code.
#
# Example output:
#   Ali <class 'str'>
#   22 <class 'int'>
#   1.75 <class 'float'>
#   True <class 'bool'>
# --------------------------------------------------------------

# Your code here
# Store personal details across four data types: str, int, float, and bool
name = "Jiya Maheshwari"
age = 19
height_m = 1.65
is_student = True

print(name, type(name))
print(age, type(age))
print(height_m, type(height_m))
print(is_student, type(is_student))


# --------------------------------------------------------------
# Task 2: Temperature Converter (Input and Typecasting)
#
# Ask the user to enter a temperature in Celsius.
# Convert the input to a float, then calculate and print the
# temperature in Fahrenheit and in Kelvin.
#
#   Fahrenheit = (Celsius * 9 / 5) + 32
#   Kelvin     = Celsius + 273.15
#
# Example output:
#   Enter temperature in Celsius: 37
#   Fahrenheit: 98.6
#   Kelvin: 310.15
# --------------------------------------------------------------

# Your code here
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")


# --------------------------------------------------------------
# Task 3: Simple Calculator (Arithmetic Operators)
#
# Ask the user to enter two numbers and convert them to floats.
# Print the result of each of these operations:
#   addition, subtraction, multiplication, division,
#   floor division, modulus and exponent (power)
#
# Example output:
#   Enter first number: 17
#   Enter second number: 5
#   Addition: 22.0
#   Subtraction: 12.0
#   Multiplication: 85.0
#   Division: 3.4
#   Floor division: 3.0
#   Modulus: 2.0
#   Power: 1419857.0
# --------------------------------------------------------------

# Your code here
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Floor division: {num1 // num2}")
print(f"Modulus: {num1 % num2}")
print(f"Power: {num1 ** num2}")


# --------------------------------------------------------------
# Task 4: Savings Tracker (Assignment Operators)
#
# Start with a variable: savings = 1000
# Then update it step by step using assignment operators
# (+=, -=, *=), printing the new value after each step:
#   1. You receive 500 as a gift          (use +=)
#   2. You spend 300 on books             (use -=)
#   3. Your savings double by year end    (use *=)
#
# Example output:
#   Starting savings: 1000
#   After gift: 1500
#   After buying books: 1200
#   After doubling: 2400
# --------------------------------------------------------------

# Your code here
savings = 1000
print(f"Starting savings: {savings}")

savings += 500
print(f"After gift: {savings}")

savings -= 300
print(f"After buying books: {savings}")

savings *= 2
print(f"After doubling: {savings}")


# --------------------------------------------------------------
# Task 5: Scholarship Check (Comparison and Logical Operators)
#
# A student qualifies for a scholarship if:
#   - their marks are 80 or more, AND
#   - their attendance is 75% or more
#
# Ask the user for their marks and attendance (convert both to
# integers). Then print True or False for each check below.
# Do not use if statements; use comparison and logical
# operators only.
#
# Example output:
#   Enter your marks: 85
#   Enter your attendance percentage: 70
#   Marks 80 or more: True
#   Attendance 75% or more: False
#   Qualifies for scholarship: False
# --------------------------------------------------------------

# Your code here
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

print("Marks >= 80:", marks >= 80)
print("Attendance >= 75:", attendance >= 75)
print("Eligible for scholarship:", (marks >= 80) and (attendance >= 75))

# ==============================================================
# Before you submit, check that:
#   [ ] Your name is written at the top of this file
#   [ ] The file is saved as yourname_task_01.py
#   [ ] The whole file runs without errors
#   [ ] Your output matches the examples
# ==============================================================
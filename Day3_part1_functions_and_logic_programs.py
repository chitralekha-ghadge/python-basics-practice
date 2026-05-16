# ============================================================
# Title       : Day 3 Part 1 - Functions and Logic Programs
# Author      : Chitralekha Ghadge
# Description : Collection of Python function programs,
#               string logic, array logic and modularity examples
# Topics      :
#   1. Maximum Consecutive Ones
#   2. Substring Count
#   3. While Loop
#   4. Functions in Python
#   5. Types of Arguments
#   6. Modularity Programs
#   7. Calculator Program
# ============================================================


# ============================================================
# FUNCTION VS METHOD
# ============================================================

# Function:
# Independent block of code
# Example:
# len(), print()

# Method:
# Function associated with object/class
# Example:
# name.upper()

# len(name) -> Function
# name.upper() -> Method


# ============================================================
# 1. MAXIMUM CONSECUTIVE ONES
# ============================================================
# Question:
# Find the maximum number of consecutive 1s in a binary array
#
# Logic:
# Iterate through the array, keeping track of current
# consecutive 1s and maximum seen so far
#
# Sample Input:
# [1,1,0,1,1,1,0,1,1,1,1]
#
# Expected Output:
# 4
# ============================================================


# ============================================================
# Method 1: Simple Loop
# ============================================================

print("\n===== MAXIMUM CONSECUTIVE ONES : METHOD 1 =====")

arr = [1,1,0,1,1,1,0,1,1,1,1]

max_count = 0
curr_count = 0

for num in arr:

    if num == 1:

        curr_count += 1

        max_count = max(max_count, curr_count)

    else:

        curr_count = 0

print("Maximum consecutive 1s:", max_count)


# ============================================================
# Method 2: Using String Conversion
# ============================================================

print("\n===== MAXIMUM CONSECUTIVE ONES : METHOD 2 =====")

arr = [1,1,0,1,1,1,0,1,1,1,1]

binary_string = ''.join(map(str, arr))

groups = binary_string.split('0')

max_ones = max(len(group) for group in groups)

print("Maximum consecutive 1s:", max_ones)


# ============================================================
# Method 3: While Loop
# ============================================================

print("\n===== MAXIMUM CONSECUTIVE ONES : METHOD 3 =====")

arr = [1,1,0,1,1,1,0,1,1,1,1]

i = 0
max_count = 0

while i < len(arr):

    count = 0

    while i < len(arr) and arr[i] == 1:

        count += 1
        i += 1

    max_count = max(max_count, count)

    i += 1

print("Maximum consecutive 1s:", max_count)


# ============================================================
# Method 4: Using itertools.groupby
# ============================================================

print("\n===== MAXIMUM CONSECUTIVE ONES : METHOD 4 =====")

from itertools import groupby

arr = [1,1,0,1,1,1,0,1,1,1,1]

max_count = 0

for key, group in groupby(arr):

    if key == 1:

        length = len(list(group))

        max_count = max(max_count, length)

print("Maximum consecutive 1s:", max_count)


# ============================================================
# Method 5: Function Based Approach
# ============================================================

print("\n===== MAXIMUM CONSECUTIVE ONES : METHOD 5 =====")

def max_consecutive_ones(arr):

    max_count = 0
    count = 0

    for num in arr:

        if num == 1:

            count += 1

            if count > max_count:

                max_count = count

        else:

            count = 0

    return max_count


arr = [1,1,0,1,1,1,0,1,1,1,1]

print("Maximum consecutive 1s:", max_consecutive_ones(arr))


# ============================================================
# Method 6: Using enumerate()
# ============================================================

print("\n===== MAXIMUM CONSECUTIVE ONES : METHOD 6 =====")

arr = [1,1,0,1,1,1,0,1,1,1,1]

max_len = 0
start = 0

for i, num in enumerate(arr):

    if num == 0:

        start = i + 1

    else:

        max_len = max(max_len, i - start + 1)

print("Maximum consecutive 1s:", max_len)


# ============================================================
# 2. COUNT SUBSTRINGS IN A STRING
# ============================================================
# Question:
# Write a program to count the number of occurrences
# of a substring in a given string
#
# Logic:
# Use loops to search for substring and count occurrences
#
# Sample Input:
# "abababab" and "ab"
#
# Expected Output:
# 4
# ============================================================


# ============================================================
# Method 1: Simple Loop
# ============================================================

print("\n===== SUBSTRING COUNT : METHOD 1 =====")

string = "abababab"
substring = "ab"

count = 0

for i in range(len(string) - len(substring) + 1):

    if string[i:i+len(substring)] == substring:

        count += 1

print("Occurrences:", count)


# ============================================================
# Method 2: Using count()
# ============================================================

print("\n===== SUBSTRING COUNT : METHOD 2 =====")

string = "abababab"
substring = "ab"

print("Occurrences:", string.count(substring))


# ============================================================
# Method 3: While Loop
# ============================================================

print("\n===== SUBSTRING COUNT : METHOD 3 =====")

string = "abababab"
substring = "ab"

count = 0
i = 0

while i <= len(string) - len(substring):

    if string[i:i+len(substring)] == substring:

        count += 1

    i += 1

print("Occurrences:", count)


# ============================================================
# 3. WHILE LOOP
# ============================================================

print("\n===== WHILE LOOP =====")

i = 1

while i <= 5:

    print(i)

    i += 1


# ============================================================
# 4. FUNCTIONS IN PYTHON
# ============================================================

print("\n===== SIMPLE FUNCTION =====")

def hello():

    print("Hello World")


hello()
hello()


# ============================================================
# 5. FUNCTION RETURNING MULTIPLE VALUES
# ============================================================

print("\n===== MULTIPLE RETURN VALUES =====")

def arithmetic():

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    sum = a + b
    sub = a - b
    div = a / b
    mul = a * b

    return sum, sub, div, mul


result = arithmetic()

print("Arithmetic =", result)

# Python returns multiple values in tuple format


# ============================================================
# TYPES OF ARGUMENTS
# ============================================================

# 1. Positional Argument
# 2. Keyword Argument
# 3. Default Argument
# 4. Variable Length Argument


# ============================================================
# 6. POSITIONAL ARGUMENT
# ============================================================

print("\n===== POSITIONAL ARGUMENT =====")

def arithmetic_operation(a, b):

    sum = a + b
    sub = a - b
    div = a / b
    mul = a * b

    return sum, sub, div, mul


result = arithmetic_operation(5, 5)

print("Arithmetic =", result)


# ============================================================
# 7. KEYWORD ARGUMENT
# ============================================================

print("\n===== KEYWORD ARGUMENT =====")

def credential(username, password):

    if username == password:

        print("Login Successfully")

    else:

        print("Invalid Credentials")


credential(username="admin", password="admin")


# ============================================================
# 8. DEFAULT ARGUMENT
# ============================================================

print("\n===== DEFAULT ARGUMENT =====")

def cityName(city="Pune"):

    print(city)


cityName("Mumbai")
cityName("Nagpur")
cityName()


# ============================================================
# 9. VARIABLE LENGTH ARGUMENT
# ============================================================

print("\n===== VARIABLE LENGTH ARGUMENT =====")

def cityNames(*name):

    print(name)


cityNames("Nagpur", "Delhi", "Mumbai", "Pune")


# ============================================================
# 10. MODULARITY APPROACH
# ============================================================

print("\n===== MODULARITY APPROACH =====")

import sys


def add():

    a = int(input('Enter value of A: '))
    b = int(input('Enter value of B: '))

    print("Addition =", a + b)


def sub():

    a = int(input('Enter value of A: '))
    b = int(input('Enter value of B: '))

    print("Subtraction =", a - b)


def div():

    a = int(input('Enter value of A: '))
    b = int(input('Enter value of B: '))

    print("Division =", a / b)


def mul():

    a = int(input('Enter value of A: '))
    b = int(input('Enter value of B: '))

    print("Multiplication =", a * b)


def mod():

    a = int(input('Enter value of A: '))
    b = int(input('Enter value of B: '))

    print("Modulus =", a % b)


while True:

    print("\n===== CALCULATOR MENU =====")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        add()

    elif choice == 2:

        sub()

    elif choice == 3:

        div()

    elif choice == 4:

        mul()

    elif choice == 5:

        mod()

    elif choice == 6:

        print("Program Exited")

        sys.exit()

    else:

        print("Invalid Choice")


# ============================================================
# END OF PROGRAM
# ============================================================
# ============================================================
# Python Day 5 Part 2
# Topics:
# 1. Dictionary Programs
# 2. String Programs
# 3. Company Based Questions
# 4. List Comprehension MCQs
# 5. Tower Of Hanoi
# ============================================================


# ============================================================
# Write a program to accept student name and marks
# and create a dictionary.
# Also display student marks by taking student name.
# ============================================================

# students = {}

# n = int(input("Enter number of students: "))

# for i in range(n):
#     name = input("Enter student name: ")
#     marks = int(input("Enter marks: "))
#     students[name] = marks

# print("Student Dictionary:", students)

# search_name = input("Enter student name to find marks: ")

# if search_name in students:
#     print(search_name, "marks are:", students[search_name])
# else:
#     print("Student not found")


# ============================================================
# Alternative Method Using get()
# ============================================================

# n = int(input("Enter the number of students: "))
# d = {}

# for i in range(n):
#     name = input("Enter student name: ")
#     marks = input("Enter Student Marks: ")
#     d[name] = marks

# while True:

#     name = input("Enter Student Name to get Marks: ")

#     marks = d.get(name, -1)

#     if marks == -1:
#         print("Student Not Found")

#     else:
#         print("The Marks of", name, "are", marks)

#     option = input("Do you want to find another student marks [Yes|No]: ")

#     if option == "No":
#         break

# print("Thanks for using our application")


# ============================================================
# Access each character of string in forward
# and backward direction using while loop
# ============================================================

# s = "Learning Python is very easy"

# print("Forward Direction:")
# i = 0

# while i < len(s):
#     print(s[i], end="")
#     i += 1

# print("\n")

# print("Backward Direction:")
# i = len(s) - 1

# while i >= 0:
#     print(s[i], end="")
#     i -= 1


# ============================================================
# Alternative Method
# ============================================================

# s = "Learning Python is very easy !!!"

# n = len(s)

# i = 0

# print("Forward Direction")

# while i < n:
#     print(s[i], end='')
#     i += 1

# print()

# print("Backward Direction")

# i = -1

# while i >= -n:
#     print(s[i], end="")
#     i -= 1


# ============================================================
# Company Question
# Find missing character in received string
# Input:
# abcdfjgerj abcdfjger
# Output:
# j
# ============================================================

# sent = input("Enter Sent String: ")
# received = input("Enter Received String: ")

# for ch in sent:
#     if sent.count(ch) != received.count(ch):
#         print("Missing Character:", ch)
#         break


# ============================================================
# Find Unique Vowels in Word
# ============================================================

# vowels = ['a', 'e', 'i', 'o', 'u']

# word = input("Enter the word: ")

# found = []

# for i in word:

#     if i in vowels:

#         if i not in found:
#             found.append(i)

# print("Found vowels =", found)

# print("Unique vowels =", len(found), "from the given word =", word)


# ============================================================
# Company Question
# Find employee distances within range
# ============================================================

# Input:
# 6 30 50
# 29 38 12 48 39 55
# Output:
# 38 48 39

# x, y, z = map(int, input().split())

# mylist = list(map(int, input().split()))

# for j in mylist:

#     if j >= y and j <= z:
#         print(j, end=' ')


# ============================================================
# MCQ Type Question - Datetime Formatting
# ============================================================

# import datetime

# date = datetime.datetime.now()

# print("It's now: {:%d/%m/%Y %H:%M:%S}".format(date))


# ============================================================
# MCQ Type Question
# Value Comparison
# ============================================================

# x = ['a', 'b', 'c', 'd']
# y = ['a', 'b', 'c', 'd']
# z = [1, 2, 3, 4]

# print(x == y)
# print(x == z)
# print(x != z)


# ============================================================
# MCQ Type Question
# List Comprehension
# ============================================================

# val = [2**i for i in range(1, 6)]

# print(val)


# ============================================================
# MCQ Type Question
# Squares using List Comprehension
# ============================================================

# s = [i*i for i in range(1, 11)]

# print(s)


# ============================================================
# MCQ Type Question
# Dictionary Comprehension
# ============================================================

# squares = {x: x*x for x in range(1, 6)}

# print(squares)


# ============================================================
# MCQ Type Question
# Double Values using Dictionary Comprehension
# ============================================================

# doubles = {x: 2*x for x in range(1, 6)}

# print(doubles)


# ============================================================
# Read Multiple Values in Single Line
# ============================================================

# a, b = [int(x) for x in input("Enter 2 numbers: ").split()]

# print("Product is:", a*b)


# ============================================================
# Read Float Values in Single Line
# ============================================================

# a, b, c = [float(x) for x in input("Enter 3 float numbers: ").split(',')]

# print("The sum is:", a+b+c)


# ============================================================
# For Else Example
# ============================================================

# mycart = [10, 20, 800, 60, 70]

# for item in mycart:

#     if item > 400:
#         print("This item is not in my budget")
#         continue

#     print(item)

# else:
#     print("You have purchased everything")


# ============================================================
# Username Password Validation
# ============================================================

# while True:

#     username = input("Enter Username: ")
#     password = input("Enter Password: ")

#     if username == "admin" and password == "admin":
#         print("Login Successful")
#         break

#     else:
#         print("Invalid Credentials")


# ============================================================
# Tower Of Hanoi Without Recursion
# Company Important Question
# ============================================================

import time

class Tower:

    def __init__(self):

        print("WELCOME TO TOWER OF HANOI GAME")
        print()

        print("Given Problem  A = [3, 2, 1]   B = []   C = []")
        print()

        print("Expected Output  A = []   B = []   C = [3, 2, 1]")
        print()

        self.A = []
        self.B = []
        self.C = []

    def tower(self, item):

        self.A.append(item)

        time.sleep(1)

        print("A =", self.A)

        print("Items in Tower A\n")

    def pass1(self):

        self.temp = self.A.pop(2)

        self.C.append(self.temp)

        time.sleep(1)

        print("A =", self.A, " B =", self.B, " C =", self.C)

        print("Pass One Completed")

    def pass2(self):

        self.temp = self.A.pop(1)

        self.B.append(self.temp)

        time.sleep(1)

        print("A =", self.A, " B =", self.B, " C =", self.C)

        print("Pass Two Completed")

    def pass3(self):

        self.temp = self.C.pop(0)

        self.B.append(self.temp)

        time.sleep(1)

        print("A =", self.A, " B =", self.B, " C =", self.C)

        print("Pass Three Completed")

    def pass4(self):

        self.temp = self.A.pop(0)

        self.C.append(self.temp)

        time.sleep(1)

        print("A =", self.A, " B =", self.B, " C =", self.C)

        print("Pass Four Completed")

    def pass5(self):

        self.temp = self.B.pop(1)

        self.A.append(self.temp)

        time.sleep(1)

        print("A =", self.A, " B =", self.B, " C =", self.C)

        print("Pass Five Completed")

    def pass6(self):

        self.temp = self.B.pop(0)

        self.C.append(self.temp)

        time.sleep(1)

        print("A =", self.A, " B =", self.B, " C =", self.C)

        print("Pass Six Completed")

    def pass7(self):

        self.temp = self.A.pop(0)

        self.C.append(self.temp)

        time.sleep(1)

        print("A =", self.A, " B =", self.B, " C =", self.C)

        print("Pass Seven Completed")


obj = Tower()

obj.tower(3)
obj.tower(2)
obj.tower(1)

obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()
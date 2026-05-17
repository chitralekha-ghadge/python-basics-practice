# ============================================================
# Title       : Python OOPs & Stack Implementation
# Author      : Chitralekha Ghadge
# Description : OOP concepts and Stack implementation using list
# Day         : Day 4 Part 1
# ============================================================


# ============================================================
# STACK IMPLEMENTATION
# ============================================================

# Stack can be implemented in two ways:
# 1. List / Array
# 2. Linked List

# Stack Operations:
# 1. Push
# 2. Pop
# 3. Peek
# 4. isEmpty
# 5. isFull
# 6. Delete
# 7. Display


# ============================================================
# CLASS AND OBJECT
# ============================================================

# Class:
# Class is a blueprint used to bind data members and methods.

# Object:
# Object is also called a reference variable.


# ============================================================
# SIMPLE CLASS PROGRAM
# ============================================================

# class Name:
#
#     age = 30
#
#     def display(self):
#         print("Hello World")
#
#
# obj = Name()
#
# print(obj.age)
#
# obj.display()


# ============================================================
# CONSTRUCTOR
# ============================================================

# Constructor automatically allocates memory for objects.

# One object creates one constructor call.

# Default Constructor Example


class Student:

    def __init__(self):

        self.name = "Chitralekha"
        self.age = 21

    def display(self):

        print("\nStudent Information")
        print("Name =", self.name)
        print("Age =", self.age)


stuObj = Student()

stuObj.display()


# ============================================================
# CONSTRUCTOR EXAMPLE
# ============================================================

class Message:

    def __init__(self):

        print("\nI am Constructor")

    def shows(self):

        print("Class Program")


obj = Message()

obj.shows()

obj2 = Message()


# ============================================================
# PARAMETERIZED CONSTRUCTOR
# ============================================================

class StudentInfo:

    def __init__(self, name, age, roll_no):

        self.Name = name
        self.Age = age
        self.RollNo = roll_no

    def displayStudentInfo(self):

        print("\nStudent Details")
        print("Name =", self.Name)
        print("Age =", self.Age)
        print("Roll No =", self.RollNo)


studentObj = StudentInfo("Chitralekha", 21, 13)

studentObj.displayStudentInfo()


# ============================================================
# STACK IMPLEMENTATION USING LIST
# ============================================================

# Stack follows:
# LIFO -> Last In First Out

# Operations:
# Push  -> Insert element
# Pop   -> Remove last element
# Peek  -> Show top element


import sys


class Stack:

    # Constructor
    def __init__(self):

        self.myStack = []

    # Push Operation
    def push(self, value):

        self.myStack.append(value)

        print("Element Pushed Successfully")

    # Display Stack
    def display(self):

        if self.myStack == []:

            print("Stack is Empty")

        else:

            print("Current Stack:", self.myStack)

    # Check Empty
    def isEmpty(self):

        if self.myStack == []:
            return True

        else:
            return False

    # Pop Operation
    def pop(self):

        if self.isEmpty():

            print("Stack is Empty")

        else:

            removed = self.myStack.pop()

            print("Removed Element:", removed)

    # Peek Operation
    def peek(self):

        if self.isEmpty():

            print("Stack is Empty")

        else:

            print("Top Element:", self.myStack[-1])

    # Delete Stack
    def deleteStack(self):

        self.myStack = []

        print("Stack Deleted Successfully")


# ============================================================
# DRIVER CODE
# ============================================================

obj = Stack()

print("\nStack has been created")


while True:

    print("\n========== STACK MENU ==========")

    print("1. Push Operation")
    print("2. Display Stack")
    print("3. Pop Operation")
    print("4. Peek Operation")
    print("5. Check Stack Empty")
    print("6. Delete Stack")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    # Push
    if choice == 1:

        value = int(input("Enter value to push in stack: "))

        obj.push(value)

    # Display
    elif choice == 2:

        obj.display()

    # Pop
    elif choice == 3:

        obj.pop()

    # Peek
    elif choice == 4:

        obj.peek()

    # isEmpty
    elif choice == 5:

        if obj.isEmpty():

            print("Stack is Empty")

        else:

            print("Stack is Not Empty")

    # Delete Stack
    elif choice == 6:

        obj.deleteStack()

    # Exit
    elif choice == 7:

        print("Program Terminated")

        sys.exit()

    else:

        print("Invalid Choice")


# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

# Q1. What is Stack?
# Stack is a linear data structure that follows LIFO.

# Q2. What is LIFO?
# Last In First Out

# Q3. Difference between Stack and Queue?
# Stack follows LIFO
# Queue follows FIFO

# Q4. Which operations are performed in Stack?
# Push, Pop, Peek, isEmpty, Delete

# Q5. Time Complexity of Push and Pop?
# O(1)

# Q6. Applications of Stack?
# - Function Calls
# - Undo Operation
# - Browser History
# - Expression Evaluation


# ============================================================
# END OF PROGRAM
# ============================================================
# ============================================================
# Title       : Python Day 4 Part 3
# Author      : Chitralekha Ghadge
# Description : Stack With Size Limit, Company Question,
#               Student Management System
# ============================================================



# ============================================================
# 1. STACK IMPLEMENTATION WITH SIZE LIMIT
# ============================================================

# import sys  

# class Stack:

#     def __init__(self, size):

#         self.mystack = []          # creating stack
#         self.stackSize = size      # stack size defined


#     def isFull(self):

#         if len(self.mystack) == self.stackSize:
#             return True

#         else:
#             return False


#     def push(self, value):

#         if self.isFull():

#             print("Stack is Full")

#         else:

#             self.mystack.append(value)

#             print("Element pushed")


#     def display(self):

#         print(self.mystack)


#     def isEmpty(self):

#         if self.mystack == []:
#             return True

#         else:
#             return False


#     def pop(self):

#         if self.isEmpty():

#             print("Stack is Empty")

#         else:

#             print(self.mystack.pop())


#     def peek(self):

#         if self.isEmpty():

#             print("Stack is Empty")

#         else:

#             print(self.mystack[-1])


#     def deleteStack(self):

#         self.mystack = None

#         print("Stack Deleted")


# size = int(input("Enter the size of stack : "))

# obj = Stack(size)

# print("Stack has created")


# while True:

#     print("1. Push Operation")
#     print("2. Display Stack")
#     print("3. Pop Operation")
#     print("4. Peek Operation")
#     print("5. Delete Stack")
#     print("7. Exit")

#     choice = int(input("Enter your choice : "))

#     if choice == 1:

#         value = int(input("Enter value to push in stack : "))

#         obj.push(value)

#     elif choice == 2:

#         obj.display()

#     elif choice == 3:

#         obj.pop()

#     elif choice == 4:

#         obj.peek()

#     elif choice == 5:

#         obj.deleteStack()

#     elif choice == 7:

#         sys.exit()

#     else:

#         print("Invalid Choice")



# ============================================================
# 2. COMPANY QUESTION
# ============================================================
# Question:
# A company wishes to encode its data.
# The data is in the form of a number.
# Count the number of times a specific digit repeats.
#
# Input :
# 572378233 3
#
# Output :
# 3
# ============================================================


# ============================================================
# Method 1
# ============================================================

# data = input("Enter Data : ")
# digit = input("Enter Digit : ")

# count = 0

# for i in data:

#     if i == digit:

#         count += 1

# print("Count =", count)



# ============================================================
# Method 2
# ============================================================

# mylist = [5,7,2,3,7,8,2,3,3]

# newdict = {}

# for i in range(len(mylist)):

#     count = 0

#     key = mylist[i]

#     j = 0

#     while j < len(mylist):

#         if key == mylist[j]:

#             count += 1

#         j = j + 1

#     if count > 1:

#         newdict[key] = count

# print(newdict)



# ============================================================
# 3. STUDENT MANAGEMENT SYSTEM
# ============================================================
# Operations:
#
# 1. Add Student
# 2. Show Student
# 3. Update Student
# 4. Delete Student
# 5. Exit
# ============================================================

import sys

student_data = {}

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. Show Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter Any Choice : "))


    # ========================================================
    # ADD STUDENT
    # ========================================================

    if choice == 1:

        student_id = int(input("Enter Student ID : "))
        roll_no = int(input("Enter Roll Number : "))
        name = input("Enter Student Name : ")
        city = input("Enter City : ")

        student_data[student_id] = {
            "RollNo": roll_no,
            "Name": name,
            "City": city
        }

        print("Student Added Successfully")


    # ========================================================
    # SHOW STUDENT
    # ========================================================

    elif choice == 2:

        if student_data == {}:

            print("No Student Data Found")

        else:

            for sid, details in student_data.items():

                print("\nStudent ID :", sid)

                for key, value in details.items():

                    print(key, ":", value)


    # ========================================================
    # UPDATE STUDENT
    # ========================================================

    elif choice == 3:

        sid = int(input("Enter Student ID To Update : "))

        if sid in student_data:

            print("1. Update Roll Number")
            print("2. Update Name")
            print("3. Update City")

            update_choice = int(input("Enter Update Choice : "))

            if update_choice == 1:

                new_roll = int(input("Enter New Roll Number : "))

                student_data[sid]["RollNo"] = new_roll

                print("Roll Number Updated")

            elif update_choice == 2:

                new_name = input("Enter New Name : ")

                student_data[sid]["Name"] = new_name

                print("Name Updated")

            elif update_choice == 3:

                new_city = input("Enter New City : ")

                student_data[sid]["City"] = new_city

                print("City Updated")

            else:

                print("Invalid Choice")

        else:

            print("Student ID Not Found")


    # ========================================================
    # DELETE STUDENT
    # ========================================================

    elif choice == 4:

        sid = int(input("Enter Student ID To Delete : "))

        if sid in student_data:

            del student_data[sid]

            print("Student Deleted Successfully")

        else:

            print("Student ID Not Found")


    # ========================================================
    # EXIT
    # ========================================================

    elif choice == 5:

        sys.exit()


    else:

        print("Invalid Choice")



# ============================================================
# END OF PROGRAM
# ============================================================
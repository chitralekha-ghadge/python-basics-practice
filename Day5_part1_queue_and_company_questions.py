# ============================================================
# DAY 5 - PART 1
# LIST STRINGS IMPORTANT MOST
# COMPANY QUESTIONS
# QUEUE DATA STRUCTURE
# ============================================================


# ============================================================
# WIPRO COMPANY QUESTION
# ============================================================

# The garments company Apparel wishes to open outlets
# at various locations.

# The company shortlisted several plots in these locations
# and wishes to select only plots that are square-shaped.

# Write an algorithm to help Apparel find the number
# of plots that it can select for its outlets.

# ============================================================
# INPUT:
# 8
# 79 77 54 81 48 34 25 16
#
# OUTPUT:
# 3
# ============================================================

import math

numOfPlots = 8

areas = [79, 77, 54, 81, 48, 34, 25, 16]

count = 0

for area in areas:

    root = int(math.sqrt(area))

    if root * root == area:

        count += 1

print("Number of Square Plots:", count)


# ============================================================
# MCQ TYPE COMPANY QUESTION
# ============================================================

# ============================================================
# Q1
# ============================================================

def func(value, values):

    var = 1

    values[0] = 44


t = 3

v = [1,2,3]

func(t, v)

print(t, v[0])

# Output:
# 3 44


# ============================================================
# Q2
# ============================================================

def f(i, values=[]):

    values.append(i)

    print(values)


f(1)

f(2)

f(3)

# Output:
# [1]
# [1, 2]
# [1, 2, 3]


# ============================================================
# QUEUE DATA STRUCTURE
# ============================================================

# Queue Operations:
# 1. EnQueue
# 2. DeQueue
# 3. Display Queue
# 4. isEmpty
# 5. isFull
# 6. Peek
# 7. Delete Queue


# ============================================================
# QUEUE IMPLEMENTATION USING LIST
# ============================================================

import sys

class Queue:

    # ========================================================
    # Constructor
    # ========================================================

    def __init__(self, size):

        self.myQueue = []

        self.queueSize = size

    # ========================================================
    # Check Queue is Full
    # ========================================================

    def isFull(self):

        if len(self.myQueue) == self.queueSize:

            return True

        else:

            return False

    # ========================================================
    # EnQueue Operation
    # ========================================================

    def enQueue(self, value):

        if self.isFull():

            print("Queue is Full")

        else:

            self.myQueue.append(value)

            print("Element Added in Queue")

    # ========================================================
    # Display Queue
    # ========================================================

    def display(self):

        print(self.myQueue)

    # ========================================================
    # Check Queue is Empty
    # ========================================================

    def isEmpty(self):

        if self.myQueue == []:

            return True

        else:

            return False

    # ========================================================
    # DeQueue Operation
    # ========================================================

    def deQueue(self):

        if self.isEmpty():

            print("Queue is Empty")

        else:

            print("Deleted Element:", self.myQueue.pop(0))

    # ========================================================
    # Peek Operation
    # ========================================================

    def peek(self):

        if self.isEmpty():

            print("Queue is Empty")

        else:

            print("Front Element:", self.myQueue[0])

    # ========================================================
    # Delete Queue
    # ========================================================

    def deleteQueue(self):

        self.myQueue = None

        print("Queue Deleted")


# ============================================================
# DRIVER CODE
# ============================================================

size = int(input("Enter the Size of Queue: "))

obj = Queue(size)

print("Queue has created")

while True:

    print()
    print("1. EnQueue Operation")
    print("2. Display Queue")
    print("3. DeQueue Operation")
    print("4. Peek Operation")
    print("5. Delete Queue")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:

        value = int(input("Enter Element to Add in Queue: "))

        obj.enQueue(value)

    elif choice == 2:

        obj.display()

    elif choice == 3:

        obj.deQueue()

    elif choice == 4:

        obj.peek()

    elif choice == 5:

        obj.deleteQueue()

    elif choice == 6:

        sys.exit()

    else:

        print("Invalid Choice")


# ============================================================
# THEORY FOR MCQ
# ============================================================

# ============================================================
# STACK USING LIST
# ============================================================

# Advantages:
# - Easy to Implement

# Disadvantages:
# - Speed Problem when Stack Grows


# ============================================================
# STACK USING LINKED LIST
# ============================================================

# Advantages:
# - Fast Performance

# Disadvantages:
# - Implementation is Difficult


# ============================================================
# STACK TIME AND SPACE COMPLEXITY
# ============================================================

#                 Time Complexity     Space Complexity

# Create Stack           O(1)               O(1)

# Push                   O(1)/O(n^2)       O(1)

# Pop                    O(1)              O(1)

# Peek                   O(1)              O(1)

# isEmpty                O(1)              O(1)

# Delete Stack           O(1)              O(1)


# ============================================================
# QUEUE USING LIST
# ============================================================

# Advantages:
# - Easy to Implement

# Disadvantages:
# - Speed Problem when Queue Grows


# ============================================================
# QUEUE USING LINKED LIST
# ============================================================

# Advantages:
# - Fast Performance

# Disadvantages:
# - Implementation is Difficult


# ============================================================
# QUEUE TIME AND SPACE COMPLEXITY
# ============================================================

#                  Time Complexity     Space Complexity

# Create Queue            O(1)              O(1)

# EnQueue                 O(1)/O(n)         O(1)

# DeQueue                 O(1)/O(n)         O(1)

# Peek                    O(1)              O(1)

# isEmpty                 O(1)              O(1)

# Delete Queue            O(1)              O(1)


# ============================================================
# MCQ TYPE QUESTION
# ============================================================

fruit = {}

def addone(index):

    if index in fruit:

        fruit[index] += 1

    else:

        fruit[index] = 1


addone('Apple')

addone('Banana')

addone('apple')

print(len(fruit))

# Output:
# 3
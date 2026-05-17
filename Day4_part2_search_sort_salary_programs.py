# ============================================================
# Title       : Python Day 4 Part 2
# Author      : Chitralekha Ghadge
# Description : Salary Programs, Binary Search, Bubble Sort,
#               Company Based Questions
# ============================================================


# ============================================================
# 1. PERFORMANCE APPRAISAL PROGRAM
# ============================================================
# Question:
# Calculate incremented salary based on employee rating.
#
# Rating 1-3   -> 10% increment
# Rating 3.1-4 -> 30% increment
# Rating 4.1-5 -> 40% increment
# ============================================================

# salary = int(input('Enter your salary : '))
# rating = float(input('Enter your performance appraisal rating : '))

# increment = 0

# if rating >=1 and rating <=3:
#     increment = salary * 10 / 100

# elif rating >=3.1 and rating <=4:
#     increment = salary * 30 / 100

# elif rating >=4.1 and rating <=5:
#     increment = salary * 40 / 100

# else:
#     print('Invalid rating')

# print('Incremented Salary :', increment + salary)



# ============================================================
# 2. GROSS SALARY CALCULATION
# ============================================================
# Question:
# Basic Salary = 20000
#
# HRA = 20%
# TA  = 30%
# DA  = 45%
#
# Calculate Gross Salary
# ============================================================

# basic_salary = 20000

# hra = basic_salary * 20 / 100
# ta = basic_salary * 30 / 100
# da = basic_salary * 45 / 100

# total_salary = basic_salary + hra + ta + da

# print("Basic Salary =", basic_salary)
# print("HRA =", hra)
# print("TA =", ta)
# print("DA =", da)
# print("Total Salary =", total_salary)



# ============================================================
# 3. BINARY SEARCH
# ============================================================
# Binary Search works only on sorted arrays.
#
# Time Complexity : O(log n)
# Space Complexity: O(1)
# ============================================================

# def binarysearch(array, target):

#     low = 0
#     high = len(array) - 1

#     while low <= high:

#         mid = (low + high) // 2

#         if array[mid] == target:
#             return mid

#         elif array[mid] < target:
#             low = mid + 1

#         else:
#             high = mid - 1

#     return -1


# array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]

# target = 72

# result = binarysearch(array, target)

# if result == -1:
#     print("Element Not Found")

# else:
#     print("Element Found at", result)



# ============================================================
# 4. BINARY SEARCH LEETCODE STYLE
# ============================================================

# class Solution(object):

#     def search(self, nums, target):

#         low = 0
#         high = len(nums) - 1

#         while low <= high:

#             mid = (low + high) // 2

#             if nums[mid] == target:
#                 return mid

#             elif nums[mid] < target:
#                 low = mid + 1

#             else:
#                 high = mid - 1

#         return -1



# ============================================================
# 5. BUBBLE SORT
# ============================================================
# Compare adjacent elements and swap them
# ============================================================

# def bubblesort(array):

#     for i in range(len(array)-1):

#         for j in range(len(array)-i-1):

#             if array[j] > array[j+1]:

#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp

#             print(array)

#         print()


# array = [64,34,25,12,22,11,90]

# bubblesort(array)



# ============================================================
# 6. SECURITY KEY COMPANY QUESTION
# ============================================================
# Question:
# A company is transmitting data to another server.
#
# Security key = count of repeating digits
#
# Input : 578378923
# Output: 3
# ============================================================


# ============================================================
# Method 1
# ============================================================

# mylist = [5,7,8,3,7,8,9,2,3]

# newlist = []

# for i in range(len(mylist)):

#     count = 0
#     key = mylist[i]

#     j = i + 1

#     while j < len(mylist):

#         if key == mylist[j]:

#             if key not in newlist:
#                 newlist.append(key)

#         j = j + 1

# print(len(newlist))



# ============================================================
# Method 2
# ============================================================

# data = input("Enter Data: ")

# visited = ""
# count = 0

# for i in range(len(data)):

#     c = 0

#     if data[i] not in visited:

#         for j in range(len(data)):

#             if data[i] == data[j]:
#                 c += 1

#         if c > 1:
#             count += 1

#         visited += data[i]

# if count == 0:
#     print(-1)

# else:
#     print(count)



# ============================================================
# 7. LINEAR SEARCH
# ============================================================
# Theory:
# Search elements one by one.
#
# Time Complexity : O(n)
# Space Complexity: O(1)
# ============================================================

# def linearSearch(array, target):

#     for i in range(len(array)):

#         if array[i] == target:
#             return i

#     return -1


# array = [10,20,30,40,50]

# target = 40

# result = linearSearch(array, target)

# if result == -1:
#     print("Target Not Found")

# else:
#     print("Target Found at Index :", result)



# ============================================================
# 8. REMOVE SPACES FROM STRING
# ============================================================

# city = input("Enter Your City Name : ")

# scity = city.strip()

# if scity == 'Hyderabad':
#     print("Hello Hyderabadi...Adab")

# elif scity == 'Chennai':
#     print("Hello Madrasi...Vanakkam")

# elif scity == 'Bangalore':
#     print("Hello Kannadiga...Shubhodaya")

# else:
#     print("Invalid City")



# ============================================================
# 9. IMPORTANT DSA THEORY NOTES
# ============================================================

# Data Structures:
# Different ways of organizing data efficiently.

# Algorithm:
# Step-by-step finite instructions to solve a problem.

# Big O Notations:
#
# O(1)       -> Constant Time
# O(n)       -> Linear Time
# O(log n)   -> Logarithmic Time
# O(n²)      -> Quadratic Time
# O(2^n)     -> Exponential Time

# Important Platforms:
#
# HackerRank:
# - Solve Me First
# - Simple Array Sum
# - Compare the Triplets
# - A Very Big Sum
# - Time Conversion
#
# LeetCode:
# - Two Sum
# - Palindrome Number
#
# HackerEarth:
# - Roy and Profile Picture

# ============================================================
# END OF PROGRAM
# ============================================================
# ============================================================
# Title       : Python DSA & Searching Practice Programs
# Author      : Chitralekha Ghadge
# Description : DSA theory, searching algorithms, string and matrix problems
# Day         : Day 3 Part 2
# ============================================================


# ============================================================
# WHAT IS DATA STRUCTURE?
# ============================================================

# Data structures are different ways of organizing data
# on a computer so that it can be used efficiently.


# ============================================================
# WHAT IS AN ALGORITHM?
# ============================================================

# Algorithm means step-by-step finite instructions
# to solve a problem.

# Properties of Algorithm:
# 1. Correctness
# 2. Efficiency


# ============================================================
# WHERE DSA IS USED?
# ============================================================

# DSA is mainly used in:
# - Software Development
# - Backend Development
# - Databases
# - Search Engines
# - Operating Systems
# - Artificial Intelligence
# - Competitive Programming

# Data Processing:
# Input -> Processing -> Output


# ============================================================
# TIME COMPLEXITY
# ============================================================

# Best Case    -> Big Omega Ω
# Average Case -> Big Theta Θ
# Worst Case   -> Big O O()


# ============================================================
# BIG O NOTATIONS
# ============================================================

# ------------------------------------------------------------
# O(1) - Constant Time
# ------------------------------------------------------------

array = [1, 2, 3, 4, 5]

print("First Element:", array[0])

# Accessing first element takes constant time


# ------------------------------------------------------------
# O(N) - Linear Time
# ------------------------------------------------------------

print("\nLinear Traversal:")

for element in array:
    print(element)

# Visiting every element once


# ------------------------------------------------------------
# O(Log N) - Logarithmic Time
# ------------------------------------------------------------

print("\nLogarithmic Example:")

for index in range(0, len(array), 2):
    print(array[index])

# Visiting selected elements only


# ------------------------------------------------------------
# O(N²) - Quadratic Time
# ------------------------------------------------------------

print("\nQuadratic Example:")

for x in array:
    for y in array:
        print(x, y)

# Nested loops


# ------------------------------------------------------------
# O(2^N) - Exponential Time
# ------------------------------------------------------------

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print("\nFibonacci:", fibonacci(5))

# Recursive Fibonacci


# ============================================================
# FIND BIGGEST NUMBER IN ARRAY
# ============================================================

def findBiggestNumber(sampleArray):

    biggestNumber = sampleArray[0]

    for index in range(1, len(sampleArray)):

        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]

    print("\nBiggest Number:", biggestNumber)


sampleArray = [5, 7, 9, 2, 3, 4]

findBiggestNumber(sampleArray)


# ============================================================
# LINEAR SEARCH
# ============================================================

# Time Complexity  -> O(N)
# Space Complexity -> O(1)

# Question:
# Search target element in array

# Input:
# [1,2,3,4,8,7,9]

# Target:
# 7

# Output:
# Target value found


def linearSearch(array, target):

    for i in range(0, len(array)):

        if array[i] == target:
            return i

    return -1


array = [1, 2, 3, 4, 8, 7, 9]

target = 7

result = linearSearch(array, target)

if result == -1:
    print("\nTarget value not found")

else:
    print("\nTarget value found at index:", result)


# ============================================================
# STRING STRIP FUNCTIONS
# ============================================================

# rstrip() -> Remove right spaces
# lstrip() -> Remove left spaces
# strip()  -> Remove both side spaces


city = input("\nEnter your City Name: ")

scity = city.strip()

if scity == 'Hyderabad':
    print("Hello Hyderabadi..Adab")

elif scity == 'Chennai':
    print("Hello Madrasi...Vanakkam")

elif scity == 'Bangalore':
    print("Hello Kannadiga...Shubhodaya")

else:
    print("Your entered city is invalid")


# ============================================================
# IMPORTANT CODING PLATFORMS
# ============================================================

# HackerRank:
# 1. Solve Me First
# 2. Simple Array Sum
# 3. Compare the Triplets
# 4. A Very Big Sum
# 5. Time Conversion

# LeetCode:
# 1. Two Sum
# 2. Palindrome Number

# HackerEarth:
# 1. Roy and Profile Picture


# ============================================================
# ROW WISE MAX VALUE IN MATRIX
# ============================================================

# Question:
# Find maximum value from every row

# Input:
# [[100,198,333,323],
#  [122,232,221,111],
#  [223,565,245,764]]

# Output:
# [333,232,764]


matrix = [
    [100, 198, 333, 323],
    [122, 232, 221, 111],
    [223, 565, 245, 764]
]

print("\nRow Wise Maximum Values:")

for row in matrix:
    print(max(row))


# ============================================================
# ROW WISE MAX VALUE - MANUAL LOGIC
# ============================================================

mylist = [
    [100, 198, 333, 323],
    [122, 232, 221, 111],
    [223, 565, 245, 764]
]

newlist = []

for i in range(3):

    j = 0

    maximum = mylist[i][j]

    for j in range(4):

        current_max = mylist[i][j]

        if maximum < current_max:
            maximum = current_max

    newlist.append(maximum)

print("\nManual Maximum List:", newlist)


# ============================================================
# MOVE * TO FRONT OF STRING
# ============================================================

# Input:
# prashant*is*a*good*programmer

# Output:
# ****prashantisagoodprogrammer


name = 'prashant*is*a*good*programmer'

newname = ''
val = ''

for i in name:

    if i != '*':
        newname += i

    else:
        val += i

print("\nModified String:")
print(val + newname)


# ============================================================
# STRING COMPRESSION
# ============================================================

# Question:
# Compress repeated characters

# Input:
# aaabbbbccceeeee

# Output:
# a3b4c3e5


s = "aaabbbbccceeeee"

result = ""

count = 1

for i in range(len(s) - 1):

    if s[i] == s[i + 1]:
        count += 1

    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

print("\nCompressed String:")
print(result)


# ============================================================
# STRING FREQUENCY USING DICTIONARY
# ============================================================

# Question:
# Count frequency of characters

# Input:
# aaabbbbccceeeee

# Output:
# a3b4c3e5


name = 'aaabbbbccceeeee'

newname = {}

for i in range(len(name)):

    key = name[i]

    count = 0

    for j in range(len(name)):

        if key == name[j]:
            count += 1

    newname[key] = count

print("\nCharacter Frequency:")

for i, j in newname.items():
    print(i, j, sep='', end=' ')


# ============================================================
# BINARY SEARCH
# ============================================================

# Question:
# Search element using Binary Search

# Condition:
# Array must be sorted

# Time Complexity:
# O(Log N)

# Input:
# [1,2,3,4,5,6,7]

# Target:
# 5


def binarySearch(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7]

target = 5

result = binarySearch(arr, target)

if result != -1:
    print("\n\nBinary Search Found at index:", result)

else:
    print("\nTarget not found")


# ============================================================
# END OF PROGRAM
# ============================================================

# ============================================================
# Title       : Python List Practice and Company Questions
# Author      : Chitralekha Ghadge
# Description : List practice programs and interview/company questions
# ============================================================


# ============================================================
# LIST BASICS
# ============================================================

mylist = ["chitra", "chitralekha", "komal", "ashish", 77, 5.34, "manthan"]

print(mylist)
print(type(mylist))

print(mylist[0])
print(mylist[1])
print(mylist[2])

print(mylist[-1])

print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[1:8:2])


# ============================================================
# UPDATE ELEMENT
# ============================================================

mylist[2] = "Akshay"

print(mylist)


# ============================================================
# SEARCH ELEMENT
# ============================================================

if "ankush" in mylist:
    print("yes ankush is available")

else:
    print('not available')


# ============================================================
# APPEND EXAMPLE
# ============================================================

mylist.append('harsh')
mylist.append('laxman')

print(mylist)

# append() and extend() both work similarly


# ============================================================
# INSERT EXAMPLE
# ============================================================

mylist.insert(3, "sanket")

print(mylist)


# ============================================================
# REMOVE EXAMPLE
# ============================================================

mylist.remove("ashish")

print(mylist)


# ============================================================
# COPY LIST
# ============================================================

newlist = mylist.copy()

print(newlist)


# ============================================================
# MULTIDIMENSIONAL LIST
# ============================================================

mylist = [['prashant', 'jha'], [85.56], [440022, "yyy"]]

print("Example of multidimensional list:")

print(mylist)

print(mylist[0][0])
print(mylist[0][1])

print(mylist[1][0])

print(mylist[2][0])
print(mylist[2][1])


# ============================================================
# DELETE EXAMPLE
# ============================================================

list2 = [50, 25.50, 'prashant']

del list2[2]

print(list2)


# ============================================================
# CLEAR LIST
# ============================================================

list2 = [50, 25.50, 'prashant']

list2.clear()

print(list2)


# ============================================================
# STRING TO LIST TYPE CASTING
# ============================================================

name = "prashant"

print(name)

myname = list(name)

print(myname)


# ============================================================
# SORTING
# ============================================================

mylist = [44, 22, 77, 0, 9, 88]

mylist.sort()

print(mylist)

mylist.sort(reverse=True)

print(mylist)

# default sorting order for numbers is ascending
# default sorting order for strings is alphabetical


# ============================================================
# ALIASING
# ============================================================

# Aliasing means assigning one variable reference to another variable

mylist = [44, 22, 77, 0, 9, 88]

newlist = mylist

print(id(mylist))
print(id(newlist))


# ============================================================
# ITERATE LIST
# ============================================================

mylist = [44, 22, 77, 0, 9, 88]

for i in mylist:
    print(i)


# ============================================================
# MOVE ZEROS TO END
# ============================================================

# Input : [0,1,4,0,2,5]
# Output: [1,4,2,5,0,0]

arr = [0, 1, 4, 0, 2, 5]

result = [x for x in arr if x != 0] + [0] * arr.count(0)

print(result)


# ============================================================
# MOVE ZEROS TO END - METHOD 2
# ============================================================

arr = [0, 1, 4, 0, 2, 5]

for i in arr:

    if i == 0:
        arr.remove(i)
        arr.append(0)

print(arr)


# ============================================================
# SECOND LARGEST ELEMENT
# ============================================================

# Question:
# Find the second largest element in an array

# Sample Input : [7,3,9,2,8]
# Expected Output : 8

arr = [7, 3, 9, 2, 8]

arr.sort()

print("Second largest:", arr[-2])


# ============================================================
# COMPANY QUESTION 1
# ============================================================

# Q1
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# Output : ValueError


# ============================================================
# COMPANY QUESTION 2
# ============================================================

# Q2
# a=[1,2,3,4,5]
# print(a[3:0:-1])

# Output : 4 3 2


# ============================================================
# COMPANY QUESTION 3
# ============================================================

# Q3

arr = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

for i in range(0, 4):
    print(arr[i].pop())

# Output:
# 4 7 11 15


# ============================================================
# COMPANY QUESTION 4
# ============================================================

arr = [1, 2, 3, 4, 5, 6]

for i in range(1, 6):
    arr[i - 1] = arr[i]

for i in range(0, 6):
    print(arr[i], end=" ")


# ============================================================
# ALIASING COMPANY QUESTION
# ============================================================

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']

fruit_list2 = fruit_list1

fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'

fruit_list3[1] = 'Kiwi'

sum = 0

for ls in (fruit_list1, fruit_list2, fruit_list3):

    if ls[0] == 'Guava':
        sum += 1

    if ls[1] == 'Kiwi':
        sum += 20

print(sum)

# Output : 22


# ============================================================
# INTERSECTION OF 3 ARRAYS
# ============================================================

# Question:
# Find the common elements in three arrays

A = [1, 2, 3]
B = [2, 3, 4]
C = [3, 4, 5]

for i in A:

    if i in B and i in C:
        print(i)


# ============================================================
# SUM OF DISTANCES BETWEEN ADJACENT NUMBERS
# ============================================================

# Write a program to calculate and return the sum of
# distances between adjacent numbers in an array

mylist = []

N = int(input("Enter the value of N : "))

for i in range(N):

    val = int(input("Enter the value : "))

    mylist.append(val)

sum = 0

for i in range(len(mylist) - 1):

    if i + 1 in range(len(mylist)):

        sum += abs(mylist[i] - mylist[i + 1])

print(sum)


# ============================================================
# END OF PROGRAM
# ============================================================
# ============================================================
# Title       : Python Strings, Patterns and Array Questions
# Author      : Chitralekha Ghadge
# Description : Collection of Python string programs, pattern
#               questions and company interview problems
# Topics      :
#   1. String Indexing and Slicing
#   2. String Methods
#   3. String Formatting
#   4. Palindrome
#   5. Vowels and Consonants
#   6. Anagram
#   7. Word Count
#   8. Pattern Programs
#   9. Array Questions
# ============================================================


# ============================================================
# 1. STRING INDEXING AND SLICING
# ============================================================

name = "Chitralekhaghadge"

print(name[0])
print(name[1])
print(name[-1])
print(name[15])

print(name[0:5])
print(name[1:])
print(name[:5])
print(name[:])

print(name[1:8:2])

print(name[::-1])      # Reverse String


# ============================================================
# 2. STRING METHODS
# ============================================================

s = "Python are High level programming Language"

print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())


# ============================================================
# 3. STRING FORMATTING
# ============================================================

name = "Chitralekha"
sal = 5000
age = 28

print("{} sal is {} age is {}".format(name, sal, age))

print("{0} sal is {1} age is {2}".format(name, sal, age))

print("{x} sal is {y} age is {z}".format(x=name, y=sal, z=age))

A = 1

print(f"{A} is a good boy")
print(f"{name} is a good boy")
print(f"{sal} is a good boy")
print(f"{age} is a good boy")


# ============================================================
# 4. PRINT EACH CHARACTER
# ============================================================

name = "chitralekha"

for i in name:
    print(i)


# ============================================================
# 5. REMOVE DUPLICATE CHARACTERS
# ============================================================

# Input  : prashant
# Output : prashnt

name = "prashant"

newname = ""

for i in name:

    if i not in newname:
        newname += i

print(newname)

print(newname[::-1])


# ============================================================
# 6. REVERSE STRING USING LOOP
# ============================================================

name = "prashant"

newname = ""

N = len(name)

for i in range(N - 1, -1, -1):

    newname += name[i]

print(newname)

print(newname[::-1])


# ============================================================
# 7. PALINDROME CHECK
# ============================================================

# Question:
# Write a program to check whether a string is palindrome or not

name = "racecar"

print(name[::-1])

if name == name[::-1]:
    print("Palindrome")

else:
    print("Not Palindrome")


# ============================================================
# 8. COUNT VOWELS AND CONSONANTS
# ============================================================

# Input  : hello
# Output : Vowels = 2 , Consonants = 3

vowels = ['a', 'e', 'i', 'o', 'u']

name = "hello"

cons = 0
vow = 0

for i in name:

    if i in vowels:
        vow += 1

    else:
        cons += 1

print("Consonants =", cons)
print("Vowels =", vow)


# ============================================================
# 9. CHECK FOR ANAGRAM
# ============================================================

# Input  : listen silent
# Output : Anagrams

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("Anagrams")

else:
    print("Not Anagrams")


# ============================================================
# 10. COUNT WORDS IN STRING
# ============================================================

# Input  : This is a sentence
# Output : 4

A = "This is a sentence"

words = A.split()

print("Total Words =", len(words))


# ============================================================
# 11. REVERSE WORDS IN STRING
# ============================================================

# Input  : Hello world
# Output : world Hello

A = "Hello world"

print(" ".join(A.split()[::-1]))


# ============================================================
# 12. BODMAS EXAMPLES
# ============================================================

a = 50
b = 30
c = 20
d = 10

print((a + b) * (c / d))

print((a - b) * (c / d))

print(a + (b * c) / d)


# ============================================================
# 13. STRING METHODS PRACTICE
# ============================================================

print('prahantjha777'.isalnum())

print('prahantjha'.isalpha())

print('777'.isdigit())

print('prahant'.islower())

print('CHITRALEKHA'.isupper())

print('My Name is Chitralekha'.istitle())

print('Hello'.startswith('He'))

print('Hello'.endswith('lo'))


# ============================================================
# 14. FIND / COUNT METHODS
# ============================================================

print('Chitralekha'.find('a'))

print('Chitralekha'.find('y'))

print('Chitralekha'.index('a'))

print('ChitralekhaGhadge'.count('a'))


# ============================================================
# 15. PATTERN PROGRAM - 111
# ============================================================

for i in range(1, 4):

    for j in range(1, 4):

        print(i, end=" ")

    print()


# ============================================================
# 16. CHARACTER PATTERN
# ============================================================

n = 4

for i in range(1, n + 1):

    for j in range(1, n + 1):

        print(chr(64 + i), end=" ")

    print()


# ============================================================
# 17. STAR PATTERN
# ============================================================

n = 5

for i in range(1, n + 1):

    for j in range(1, i + 1):

        print("*", end=" ")

    print()


# ============================================================
# 18. ALPHABET PATTERN
# ============================================================

n = 5

for i in range(1, n + 1):

    for j in range(1, n + 1):

        print(chr(64 + j), end=" ")

    print()


# ============================================================
# 19. PYRAMID PATTERN
# ============================================================

n = 5

for i in range(1, n + 1):

    print(" " * (n - i), end=" ")

    for j in range(1, i + 1):

        print("*", end=" ")

    print()


# ============================================================
# 20. PRODUCT OF ARRAY EXCEPT SELF
# ============================================================

# Input  : [1,2,3,4]
# Output : [24,12,8,6]

nums = [1, 2, 3, 4]

n = len(nums)

result = [1] * n


# Left Pass
left = 1

for i in range(n):

    result[i] = left

    left *= nums[i]


# Right Pass
right = 1

for i in range(n - 1, -1, -1):

    result[i] *= right

    right *= nums[i]

print(result)


# ============================================================
# END OF PROGRAM
# ============================================================
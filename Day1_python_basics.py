# ============================================================
# Title       : Python Basics Practice Programs
# Author      : Chitralekha Ghadge
# Description : Collection of beginner Python programs
# Topics      :
#   1. Data Types
#   2. Type Casting
#   3. Conditional Statements
#   4. Operators
#   5. Loops
#   6. Zip Function
# ============================================================


# ============================================================
# 1. DATA TYPES IN PYTHON
# ============================================================

age = 21
pi = 3.14
name = "Chitralekha"
result = True

print("===== DATA TYPES =====")
print(type(age))
print(type(pi))
print(type(name))
print(type(result))


# ============================================================
# 2. MEMORY ID EXAMPLES
# ============================================================

print("\n===== MEMORY IDs =====")
print(id(age))
print(id(pi))
print(id(name))
print(id(result))


# ============================================================
# 3. IMMUTABLE DATATYPE EXAMPLE
# ============================================================

math = 50
chem = 50
phy = 50

print("\n===== IMMUTABLE DATATYPE =====")
print(id(math))
print(id(chem))
print(id(phy))


# ============================================================
# 4. SIMPLE INPUT WITHOUT TYPE CASTING
# ============================================================

print("\n===== STRING INPUT EXAMPLE =====")

a = input("Enter first number : ")
b = input("Enter second number : ")

print("Result :", a + b)      # String concatenation


# ============================================================
# 5. INPUT WITH TYPE CASTING
# ============================================================
# print(2+2)
# print("2"+"2")
#-------------------------------------------------------------
print("\n===== INTEGER INPUT EXAMPLE =====")

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Addition :", a + b)


# ============================================================
# 6. INTEGER TYPE CASTING
# ============================================================

print("\n===== int() TYPE CASTING =====")

print(int(3.14))
print(int(True))
print(int(False))
print(int("4"))


# ============================================================
# 7. FLOAT TYPE CASTING
# ============================================================

print("\n===== float() TYPE CASTING =====")

print(float(3))
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))


# ============================================================
# 8. COMPLEX TYPE CASTING
# ============================================================

print("\n===== complex() TYPE CASTING =====")

print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))

print(complex("5"))
print(complex("5.6"))

print(complex(5, -3))
print(complex(True, False))


# ============================================================
# 9. BOOLEAN TYPE CASTING
# ============================================================

print("\n===== bool() TYPE CASTING =====")

print(bool(0))
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(1 + 2j))
print(bool(0 + 0j))
print(bool(-1))
print(bool("False"))
print(bool("True"))


# ============================================================
# 10. SIMPLE IF CONDITION
# ============================================================

print("\n===== POSITIVE / NEGATIVE / ZERO =====")

num = int(input("Enter any number : "))

if num > 0:
    print("Positive")

if num < 0:
    print("Negative")

if num == 0:
    print("Zero")


# ============================================================
# 11. WORKING DAY / WEEKEND
# ============================================================

print("\n===== WORKING DAY CHECK =====")

day = input("Enter a day : ").lower()

if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("Working Day")
else:
    print("Weekend")
#-------------------------------------------------------------
print("\n===== WORKING DAY CHECK =====")

day = input("Enter a Day: ")

if day == "SATURDAY" or day == "saturday" or day == "SUNDAY":
     print("WEEKEND")
else:
     print("Working day")

# ============================================================
# 12. GRADE SYSTEM
# ============================================================

print("\n===== GRADE SYSTEM =====")

per = 65

if per >= 65:
    print("Grade A")

elif per >= 50:
    print("Grade B")

else:
    print("Fail")


# ============================================================
# 13. CHARACTER CHECK PROGRAM
# ============================================================
# A = 65
# a = 97
# 0 = 48
print("\n===== CHARACTER CHECK =====")

char = ord(input("Enter one character : "))

if char >= 65 and char <= 90:
    print("Upper Case")

elif char >= 97 and char <= 122:
    print("Lower Case")

elif char >= 48 and char <= 57:
    print("Digit")

else:
    print("Special Symbol")


# ============================================================
# 14. MEMBERSHIP OPERATOR
# ============================================================

print("\n===== MEMBERSHIP OPERATOR =====")

name = "help4code"

print('p' in name)
print('p' not in name)


# ============================================================
# 15. IDENTITY OPERATOR
# ============================================================

print("\n===== IDENTITY OPERATOR =====")

math = 50
chem = 50

print(math is chem)
print(math is not chem)


# ============================================================
# 16. FOR LOOP EXAMPLES
# ============================================================
#for(initialization; condition;incre/decre)

print("\n===== FOR LOOP EXAMPLES =====")

for i in range(5):
    print(i)

print()

for i in range(2, 10):
    print(i)

print()

for i in range(2, 10, 3):
    print(i)

print()

for i in range(5, 0, -1):
    print(i)

for i in range(5,0):
     print(i)

# ============================================================
# 17. MULTIPLICATION TABLE OF 2
# ============================================================

print("\n===== TABLE OF 2 =====")

for i in range(1, 11):
    print(i * 2)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Q2 3 4 5 6 7 8 9 10

# --------------------

# 11 12 13 14 15...20

# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)
#     print()
# for i in range(1,11):
#     print(i*11," ", i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)


# ============================================================
# 18. STUDENT RESULT PROGRAM
# ============================================================
# write a program accept 3 paper marks and 
# calculate, percent and check if he/she is passed in all the subject
# so print pass else print fail  
# if percent is greater than 65 and gender="male" so he is eligible for placement else not eligible

print("\n===== STUDENT RESULT =====")

phy = int(input("Enter Physics Marks : "))
chem = int(input("Enter Chemistry Marks : "))
math = int(input("Enter Maths Marks : "))

total = phy + chem + math
percentage = total / 3.0

print("Total =", total)
print("Percentage =", percentage)

if phy >= 40 and chem >= 40 and math >= 40:
    print("Pass")
else:
    print("Fail")

gender = input("Enter Gender (M/F) : ")

if percentage >= 65 and gender == "M":
    print("Eligible For Placement")
else:
    print("Not Eligible")


# ============================================================
# 19. BREAK STATEMENT
# ============================================================

print("\n===== BREAK STATEMENT =====")

for i in range(1, 5):

    if i == 3:
        break

    print(i)


# ============================================================
# 20. CONTINUE STATEMENT
# ============================================================

print("\n===== CONTINUE STATEMENT =====")

for i in range(1, 5):

    if i == 3:
        continue

    print(i)


# ============================================================
# 21. ZIP FUNCTION EXAMPLE
# ============================================================
#Question
# 1  5
# 2  4
# 4  2
# 5  1

print("\n===== ZIP FUNCTION =====")

for i, j in zip(range(1, 6), range(5, 0, -1)):

    if i == 3 and j == 3:
        continue

    print(i, " ", j)


# ============================================================
# END OF PROGRAM
# ============================================================
# ============================================================
# Title       : Day 2 Part 2 - Tuple, Dictionary & Logic Programs
# Author      : Chitralekha Ghadge
# Description : Collection of Python tuple, dictionary, pattern,
#               string and logic building programs
# Topics      :
#   1. Tuple Programs
#   2. Dictionary Programs
#   3. Reverse Number Logic
#   4. Frequency Count
#   5. String Programs
#   6. Pattern Programs
#   7. ATM Withdrawal Logic
#   8. Interview Questions
# ============================================================


# ============================================================
# 1. TUPLE DATATYPE
# ============================================================

print("\n===== TUPLE DATATYPE =====")

mytuple = (
    "prashant",
    "Ashish",
    "Rahul",
    "Sandip",
    "Komal",
    "Ankush",
    "Rajesh",
    23,
    3.15,
    77,
    "Sandip"
)

print(mytuple)
print(type(mytuple))


# ============================================================
# 2. EMPTY TUPLE
# ============================================================

print("\n===== EMPTY TUPLE =====")

init_tuple = ()
print(init_tuple.__len__())


# ============================================================
# 3. TUPLE COMPARISON
# ============================================================

print("\n===== TUPLE COMPARISON =====")

init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')

print(init_tuple_a == init_tuple_b)


# ============================================================
# 4. TUPLE CONCATENATION
# ============================================================

print("\n===== TUPLE CONCATENATION =====")

init_tuple_a = ('1', '2')
init_tuple_b = ('3', '4')

print(init_tuple_a + init_tuple_b)


# ============================================================
# 5. TUPLE MULTIPLICATION
# ============================================================

print("\n===== TUPLE MULTIPLICATION =====")

init_tuple = ('Python',) * 3

print(init_tuple)
print(type(init_tuple))


# ============================================================
# 6. TUPLE VS STRING
# ============================================================

print("\n===== TUPLE VS STRING =====")

value = ('Python') * 3

print(value)
print(type(value))


# ============================================================
# 7. TUPLE SLICING
# ============================================================

print("\n===== TUPLE SLICING =====")

init_tuple = ((1, 2),) * 7

print(len(init_tuple[3:8]))


# ============================================================
# 8. DICTIONARY DATATYPE
# ============================================================

print("\n===== DICTIONARY DATATYPE =====")

mydict = {
    101: "prashant",
    102: "ashish",
    "103": "mohini",
    "104": "triveni",
    101: "ashish",
    104: "ashish"
}

print(mydict)


# ============================================================
# 9. ACCESSING DICTIONARY VALUES
# ============================================================

print("\n===== ACCESSING VALUES =====")

print(mydict[102])


# ============================================================
# 10. UPDATE DICTIONARY VALUE
# ============================================================

print("\n===== UPDATE VALUE =====")

mydict[102] = "peter"

print(mydict)


# ============================================================
# 11. PRINT ONLY KEYS
# ============================================================

print("\n===== ONLY KEYS =====")

for x in mydict:
    print(x)


# ============================================================
# 12. PRINT ONLY VALUES
# ============================================================

print("\n===== ONLY VALUES =====")

for x in mydict.values():
    print(x)


# ============================================================
# 13. PRINT KEYS AND VALUES
# ============================================================

print("\n===== KEYS AND VALUES =====")

for x, y in mydict.items():
    print(x, y)


# ============================================================
# 14. ADD NEW VALUE IN DICTIONARY
# ============================================================

print("\n===== ADD NEW VALUE =====")

mydict["mobile_no"] = 4646463738

print(mydict)


# ============================================================
# 15. TUPLE AS DICTIONARY KEY
# ============================================================

print("\n===== TUPLE AS KEY =====")

a = {(1, 2): 1, (2, 3): 2, (4, 5): 3}

print(a[4, 5])


# ============================================================
# 16. DICTIONARY NUMBER LOGIC
# ============================================================

print("\n===== DICTIONARY NUMBER LOGIC =====")

arr = {}

arr[1] = 1
arr['1'] = 2
arr[1] += 1

print(arr)

sum = 0

for k in arr:
    sum += arr[k]

print(sum)


# ============================================================
# 17. FLOAT AND INTEGER KEY LOGIC
# ============================================================

print("\n===== FLOAT AND INTEGER KEY =====")

my_dict = {}

my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4

print(my_dict)

sum = 0

for k in my_dict:
    sum += my_dict[k]

print(sum)


# ============================================================
# 18. TUPLE KEY SUM
# ============================================================

print("\n===== TUPLE KEY SUM =====")

my_dict = {}

my_dict[(1, 2, 4)] = 8
my_dict[(4, 2, 1)] = 10
my_dict[(1, 2)] = 12

sum = 0

for k in my_dict:
    sum += my_dict[k]

print(sum)
print(my_dict)


# ============================================================
# 19. DICTIONARY LENGTH
# ============================================================

print("\n===== DICTIONARY LENGTH =====")

box = {}
jars = {}
crates = {}

box['biscuit'] = 1
box['cake'] = 3

jars['jam'] = 4

crates['box'] = box
crates['jars'] = jars

print(len(crates['box']))


# ============================================================
# 20. SORTED DICTIONARY
# ============================================================

print("\n===== SORTED DICTIONARY =====")

dict_data = {'c': 97, 'a': 96, 'b': 98}

for i in sorted(dict_data):
    print(dict_data[i])


# ============================================================
# 21. DICTIONARY COPY
# ============================================================

print("\n===== DICTIONARY COPY =====")

rec = {"Name": "Python", "Age": "20"}

r = rec.copy()

print(id(r) == id(rec))


# ============================================================
# 22. FIND MAX VALUE KEY
# ============================================================

print("\n===== MAX VALUE KEY =====")

data = {"A": 50, "B": 30, "C": 70}

max_key = max(data, key=data.get)

print(max_key)


# ============================================================
# 23. FIND MIN VALUE KEY
# ============================================================

print("\n===== MIN VALUE KEY =====")

data = {"X": 20, "Y": 10, "Z": 30}

min_key = min(data, key=data.get)

print(min_key)


# ============================================================
# 24. COUNT FREQUENCY USING DICTIONARY
# ============================================================

print("\n===== FREQUENCY COUNT =====")

numbers = [1, 2, 2, 3, 4, 3, 5]

freq = {}

for item in numbers:

    if item in freq:
        freq[item] += 1

    else:
        freq[item] = 1

print(freq)


# ============================================================
# 25. REVERSE NUMBER (3 DIGIT)
# ============================================================

print("\n===== REVERSE 3 DIGIT NUMBER =====")

num = 123

a = num % 10
num = num // 10

b = num % 10

c = num // 10

rev = a * 100 + b * 10 + c

print(rev)


# ============================================================
# 26. REVERSE NUMBER USING LOOP
# ============================================================

print("\n===== REVERSE NUMBER USING LOOP =====")

num = 123456

rev = 0

while num > 0:

    digit = num % 10

    rev = rev * 10 + digit

    num = num // 10

print(rev)


# ============================================================
# 27. ANAGRAM CHECK
# ============================================================

print("\n===== ANAGRAM CHECK =====")

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("Anagrams")

else:
    print("Not Anagrams")


# ============================================================
# 28. COUNT WORDS IN STRING
# ============================================================

print("\n===== COUNT WORDS =====")

text = "This is a sentence"

words = text.split()

print("Total Words =", len(words))


# ============================================================
# 29. REVERSE WORDS IN STRING
# ============================================================

print("\n===== REVERSE WORDS =====")

text = "Hello World"

words = text.split()

reverse_text = words[::-1]

print(" ".join(reverse_text))


# ============================================================
# 30. SPECIAL CHARACTER COUNT
# ============================================================

print("\n===== SPECIAL CHARACTER COUNT =====")

text = "gasgg54@#vscsd!s*"

count = 0

for i in text:

    value = ord(i)

    if not (
        (value >= 65 and value <= 90) or
        (value >= 97 and value <= 122) or
        (value >= 48 and value <= 57)
    ):

        count += 1

print("Special Characters =", count)


# ============================================================
# 31. PATTERN PROGRAM
# ============================================================

print("\n===== NUMBER PATTERN =====")

for i in range(1, 4):

    for j in range(1, 4):

        print(i, end=" ")

    print()


# ============================================================
# 32. STAR PATTERN
# ============================================================

print("\n===== STAR PATTERN =====")

n = 5

for i in range(1, n + 1):

    for j in range(1, i + 1):

        print("*", end=" ")

    print()


# ============================================================
# 33. PRODUCT OF ARRAY EXCEPT SELF
# ============================================================

print("\n===== PRODUCT OF ARRAY EXCEPT SELF =====")

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
# 34. ATM WITHDRAWAL PROGRAM
# ============================================================

print("\n===== ATM WITHDRAWAL =====")

Amount = int(input("Please Enter Amount For Withdraw : "))

print("100 notes =", Amount // 100)

print("50 notes =", (Amount % 100) // 50)

print("20 notes =", ((Amount % 100) % 50) // 20)

print("10 notes =", (((Amount % 100) % 50) % 20) // 10)

print("5 notes =", ((((Amount % 100) % 50) % 20) % 10) // 5)

print(
    "2 notes =",
    (((((Amount % 100) % 50) % 20) % 10) % 5) // 2
)

print(
    "1 notes =",
    ((((((Amount % 100) % 50) % 20) % 10) % 5) % 2) // 1
)


# ============================================================
# END OF PROGRAM
# ============================================================
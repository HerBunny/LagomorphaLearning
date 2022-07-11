#elif bmi <= 25:
#    print("Overweight")
#elif bmi <= 18.5:
#    print("Normal")
#else:
#    print("Underweight")

### Basic Operators ###

a = 10
b = 21

print("--- Arithmetic ---")

print("Addition: " + str(a + b))
print("Subtraction: " + str(a - b))
print("Multiplication: " + str(a * b))
print("Division: " + str(b / a))
print("Modulus: " + str(b % a))
print("Exponant: " + str(a**b))
print("Floor: " + str(b // a))

print("--- Comparisons ---")

print("Equal to: " + str(a == b))
print("Not equal to: " + str(a != b))
print("Greater than: " + str(a > b))
print("Less than: " + str(a < b))
print("Greater than or equal to: " + str(a >= b))
print("Less than or equal to: " + str(a <= b))

print("--- Assignment ---")

a = 6_418_372.00
b = 3_888_497.00

print(a + b)

### Lists ###

print("--- Lists ---")

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

print("--- Different Data Types ---")

x = ["a","b","c"]
y = [1, 2, 3, 4, 5]

print(x[1])
print(y[3])

print("--- Nested Lists ---")

m = [
    [1, 2, 3],
    [4, 5, 6]
    ]

print(m[1][2]) # List, Row, Element Number

print("--- Strings ---")

str = "Hello World!"
print(str[6])

print("--- Print 3rd Element of input")

print(input("Please enter some text: ")[2])

print("### List Operations ###")

print("--- Reassigning Element Values")

nums = [5, 8, 2]
print(nums)
nums[1] = 42
print(nums)

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums + [7, 8, 9])

nums += [4, 5, 6]
nums += [7, 8, 9]

print(nums)

print(6//2)

print("---------")

nums = [1, 2, 3]
print(nums * 3)

print("---------")

words = [
    "spam",
    "egg",
    "spam",
    "sausage"
    ]

print("spam" in words)
print("egg" in words)
print("tomato" in words)

print("---------")

x = "hello world"
if "o w" in x:
    print("Yes")

print("---------")

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

print("### for Loops")

words = [
    "hello",
    "world",
    "spam",
    "eggs"
    ]

for word in words:
    print(word + "!")

print("---------")

nums = [4, 7, 3, 1]
for x in nums:
    print(x*2)

print("---------")

str = "testing for loops"
count = 0

for x in str:
    if x == 't':
        count += 1

print(count)

print("---------")

text = "some text"

for x in text:
    if x == 'e':
        break
    print(x)

print("### Ranges ###")

numbers = list(range(10))

for num in numbers:
    print(num)

print(numbers)

print("---------")

numbers = list(range(3, 8))
print(numbers)

print("---------")

numbers = list(range(5, 20, 2))
print(numbers)

print("---------")

x = list(range(7, 3, -1))
print(x)

print("---------")

for i in range(5):
    print("Hello!")

print("### List Slices ###")

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
print(squares[:7])
print(squares[7:])
print(squares[::2])
print(squares[2:8:3])
print(squares[1:-2])

res = squares[::-1]
print(res)

names = ["Iain", "James", "Gary", "Mike", "Stewart"]

print(names[1:-1])

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

print("### Functions ###")

nums = [1, 3, 5, 2, 4]
print(len(nums))

str = "some text"
x = len(str)
print(x)

nums = [1, 2, 3]
nums.append(4)
print(nums)
# Outputs: [1, 2, 3, 4]

words = ["Python", "fun"]
words.insert(1, "is")
print(words)
# Outputs: ["Python", "is", "fun"]

letters = ["p", "q", "r", "s", "p", "u"]
print(letters.index("r"))
print(letters.index("p"))
print(letters.index("q"))
# Outputs: 
# 2 
# 0
# 1

x = [1, 8, 42, 3]
print(min(x))
print(max(x))
# Outputs:
# 1
# 42


x = [2, 4, 6, 2, 7, 2, 9]
print(x.count(2))

x.remove(4)
print(x)

x.reverse()
print(x)
# Outputs:
# 3
# [2, 6, 2, 7, 2, 9]
# [9, 2, 7, 2, 6, 2]

while 2 in x:
    x.remove(2)
    print(x)

nums = [4,5,6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)
# Output: Numbers: 4 5 6

a = "{x}, {y}".format(x=5, y=12)
print(a)
# Output: 5, 12

x = ", ".join(["spam", "eggs", "ham"])
print(x)
# Output: spam, eggs, ham

str = "some text goes here"
x = str.split(" ")
print(x)
# Output: ['some', 'text', 'goes', 'here']

x = "Hello ME"
print(x.replace("ME", "world"))
# Output: Hello world

x = "HeLLo world"
print(x.replace("L", "l"))
# Output: Hello world

print("This is a sentence.".upper())
print("AN ALL CAPS SENTENCE".lower())
# Output: 
# THIS IS A SENTENCE
# an all caps sentence

print("<<<!!! End of Script !!!>>>")
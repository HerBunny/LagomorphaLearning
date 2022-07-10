if not True:
    print("1")
elif not (1+1 == 3):
    print("2")
else:
    print("3")

print("--- Chaining Booleans ---")
country = "US"
age = 42

if (country == "US" or country == "GB") and (age > 0 and age < 100):
    print("Cool")

# Python order of math
    # parentheses
    # exponentiation
    # multiplication / division
    # addition subtraction

print(1+1*3)

### Break & Continue ###

print("--- Break ---")

i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")

i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break


print("--- Continue ---")

i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping 3")
        continue
    print(i)

i = 0
while True:
    i += 1
    if (i == 2):
        continue
    if (i == 5):
        break

    print(i)

fares = 100
passengers = []
takings = 0

while len(passengers) < 5:
    user_input = int(input())
    passengers.append(user_input)

for passenger in passengers:
    if passenger < 3:
        continue
    takings += fares

print(takings)

weight = float(input())
height = float(input())
bmi = weight / height**2

if bmi > 30:
    print("Obesity")
elif bmi <= 25:
    print("Overweight")
elif bmi <= 18.5:
    print("Normal")
else:
    print("Underweight")

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

print("<<<!!! End of Script !!!>>>")
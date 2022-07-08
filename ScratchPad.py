# Scratch Pad

### Loops ###

print("--- While Loops ---")

x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
    x += 1

print("---------")

sum = 0
x = 10
while x > 0:
    sum += x
    x -= 1

print(sum)

print("---------")

x = 0
while x < 10:
    print(x)
    x += 1

print("---------")

i = 1
while i <= 5:
    print(i)
    i = i + 1

print(str(i) + "Finished!")

### Boolean Logic ###

print("--- And operator ---")
print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(2 < 1 and 3 > 6)

# Or operator
print(1 == 1 or 2 == 2)
print(1 == 1 or 2 == 3)
print(1 != 1 or 2 == 2)
print(2 < 1 or 3 > 6)

# Compare variables
age = 24
limit = 18
height = 191

if (age > limit and height > 180):
    print("Yes")

# Boolean Not
print(not 1 == 1)
print(not 1 > 7)

# WTF???
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
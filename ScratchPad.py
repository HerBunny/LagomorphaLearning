# Python3 Scratch Pad

def python_core():
    def strings_and_variables():
        """
        Working with Input*
        In-Place and Walrus Operations*
        Module 2 Quiz
        Simple Calculator Coding Project
        """
    def control_structures():
        """
        Booleans & Comparisons
        If Statements
        Boolean Logic
        Multiple Operators & ...
        Lists
        List Operations
        List Functions
        While Loops
        For Loops
        Range
        Module 3 Quiz
        FizzBuzz
        """
    def functions_and_modules():
        """
        Code Reuse
        Functions
        Function Arguments
        Returning from Functions
        Comments & Docstrings
        Functions as Objects
        Modules
        The Standard Library & pip
        Module 4 Quiz
        Celsius to Fahrenheit Converter Project
        """
    def exceptions_and_files():
        """
        41.1 - Exceptions
        42.1 - Exception Handling
        42.2 - Bank card PIN System
        43.1 - finally
        43.2 - Making Coffee
        44.1 - Raising Exceptions
        45.1 - Assertions
        45.2 - ???
        46.1 - Opening Files
        46.2 - ???
        47.1 - Reading Files
        47.2 - Getting in Shape
        48.1 - Writing Files
        48.2 - New Lines
        49.1 - Working with Files
        50.1 - Module 5 Quiz
        51 - Code Project: Book Titles
        """

nums = [4, 5, 6]
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

### Module Imports ###

### Functions ###

def congrats(name, count, course):
    print(f"Congrats {name}, on achieving your {count} certificate in {course}!!!")

def thefirst(): 
    print(defvar)

def my_func():
    print("spam")
    print("spam")
    print("spam")

def hello():
    print("Hello world!")

def exclaimation(word):
    print(word + "!")

def print_sum_twice(x, y):
    print(x + y)    
    print(x + y)

def sum(x, y):
    return x + y

def max(x, y):
    if x >= y:
        return x
    else:
        return y

def add_numbers(x, y):
    total = x + y
    return total
    print("This line shall not pass!!!")

def double(a, b):
    return [a*2, b*2]        

def words_list(list):
    print(list[0])
    print(list[1])
    print(list[2])    

def a_comment():
    x = 365
    y = 7

    print(x % y) # find the remainder

def multi_comment():
    x = 42
    y = 9
    # this is a comment

    print(x % y) # find the remainder
    # print (x // y)
    # another comment

def shout(word):
    """
    Print a word with an 
    exclaimation mark following it.
    """
    print(word + "!")

def print_calculations(a, b, c, d, e):
    print(a + b)
    print(c + d - e)

def order_of_operations(a, b, c, d, e):
    print(a * (b + c))
    print(d / e)

def exponentiation(x, y):
    """
    Raises x to the power of y.
    """
    return x**y

def sqr_root(x):
    """
    Returns the square root of a number.
    """
    return (x ** (1/2))

def divide_and_conquer(x, y):
    """
    Performs division using the two inputs,
    then outputs the quotient and remainder.
    """
    q = int(x // y)
    r = int(x % y)
    print(f"The result of dividing {int(x)} by {int(y)} is that...")
    print(f"{int(y)} goes into {int(x)}, {q} times.")
    print(f"With a remainder of {r}")    

def tag():
    print("     👨‍💻      🐇")
    print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    print("⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛")
    print("⬛⬛⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛")
    print("⬛⬛⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛")
    print("⬛⬛⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛")
    print("⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛")
    print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")

def strings():
    print("Python is fun!")
    print('Always look on the bright side of life')

def backslash():
    print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')

def newlines():
    print('One\nTwo\nThree')

def multiline_text():
    print("""this
    is a
    multiline
    text""")

def concatenation():
    print("Spam" + 'eggs')
    print("2" + "2")

def string_operations():
    print("Spam" * 3)
    print(4 * '2')

def corresponding_ops(y):
    """
    Variables can be used to perform corresponding operations.
    """
    print("Corresponding Ops:")
    
    x = 7
    print(x)

    print(x + y)
    print(x)

    #> 7
    #> 47
    #> 7

    input("\nHit enter to Continue")

def variable_reassignment():
    """
    Variables don't have a specific data type. They can be changed to other types as needed.
    """
    print("Variable Reassignment: ")

    x = 123.456
    print(f"x = {x}")

    x = "This is a string"
    print(f'x = {x + "!"}')

    #> x = 123.456
    #> x = This is a string!

    input("\nHit enter to Continue")

def user_input():
    """
    The intuitively named input function, is used to get an input from the user.
    """
    print("User Input:")

    x = input("Enter something: ")
    print(f"You typed: {x}")

    #> User Input:
    #> You typed: [your input here]

    input("\nHit enter to continue...")

def user_input_2():
    """
    User inputs must be followed by parentheses. A prompt may be given within the parenthesis.
    """
    print("User input 2:")

    name = input("Enter your name: ")
    print(f"Hello {name}. Good to meet you. :)")

    #> Enter your name:
    #> Hello [your name]. Good to meet you. :)

    input("\nHit enter to continue...")


words = ["Hello", "world", "!"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
           "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]
punctuation = [",", ".", "!", "?"]

defvar = "Oh, Yeah!!!"
a = 2
b = 2
c = 5
d = 4
e = 3


if __name__ == "__main__":
    # Code to execute when run directly

    print("Congrats:")
    congrats("Iain", "First", "Python for Beginners")    
    input("\n Press the enter key to continue")

    corresponding_ops(40)
    variable_reassignment()
    user_input()
    user_input_2()

    print("<<<!!! End of Script !!!>>>")
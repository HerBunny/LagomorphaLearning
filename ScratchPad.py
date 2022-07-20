# Python3 Scratch Pad

def python_core():
    def control_structures():
        """
        Booleans & Comparisons*
        If Statements*
        At The Boiling Point
        else Statements*
        Club Bouncer Code*
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
        51.1 - Code Project: Book Titles
        """
    def more_types():
        """
        52.1 - None
        53.1 - Dictionaries
        53.2 - Inventory Management
        54.1 - Dictionary Functions
        54.2 - Where's The Book?
        55.1 - Tuples
        55.2 - Tuples
        56.1 - List Slices
        56.2 - List Slices
        57.1 - List Comprehensions
        57.2 - List of Multiples
        58.1 - String Formatting
        58.2 - Names and Ages
        59.1 - Useful Functions
        59.2 - Broken Keyboard
        60.1 - Text Analyzer
        60.2 - How many words?
        61.1 - Module 6 Quiz
        62 - Longest Word
        """
    def functional_programming():
        """
        63.1 - Functional programming
        63.2 - ???
        64.1 - Lambdas
        64.2 - Lambdas
        65.1 - map & filter
        65.2 - Filtering
        66.1 - Generators
        66.2 - Split Generator
        67.1 - Decorators
        67.2 - Uppercasing
        68.1 - Recusion
        68.2 - Fun With Math
        69.1 - Sets
        69.2 - Commonality
        70.1 - intertools
        70.2 - Ordering
        71.1 - Module 7 Quiz
        72 - Fibernacci Code Project
        """

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
    """
    Just for fun, way of marking milestones in my learning journey. ;)
    """
    print("Congrats:")
    
    print(f"Congrats {name}, on achieving your {count} certificate in {course}!!!")

    input("\nHit enter to continue...")

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

    input("\nHit enter to Continue...")

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

def str_as_int():
    """
    Inputs are strings by default, though they can be converted to an integer, for use in calculations.
    """
    print("String inputs as Integers: ")

    age = int(input("Enter your age: "))
    print(age)
    print(int(age/2))
    print(f"Your age is {age}")

    #> [Integer you entered]
    #> [Half of the integer value, you entered]
    #> Your age is [Integer you entered]    

    input("\nHit enter to continue...")

def name_and_age():
    """
    Taking an input for name & age, and then using that to output a response.
    """
    print("Name and Age: ")

    name = input("What is your name? ")
    age = input("How old are you? ")

    print(f"{name} is {age} years old.")

    #> {name} is {age} years old.

    input("\nHit enter to continue...")

def multiple_variables():
    """
    Code coach exercize
    """
    print("Code Coach: Multiple Variables: ")
    
    x = input()
    y = input()

    print(x * int(y))

    #> xxx...

    input("\nHit enter to continue...")
    
def in_place_operators():
    """
    In-place operators allow for more concise coding.
    """
    print("In-Place operators:")

    x = 2
    print(f"setting initial value for x: {x}")

    x += 3
    print(f"Adding 3 to x: {x}")

    x *= 3
    print(f"Multiplying x by 3: {x}")

    x /= 3
    print(f"Dividing x by 3: {x}")

    input("\nHit enter to continue...")

def spam_and_eggs():
    """
    What's a little spam, without eggs? ;)
    """
    print("Spam and Eggs:")

    x = "spam"
    print(x)

    x += "eggs"
    print(x)

    #> spam
    #> spameggs

    input("\nHit enter to continue...")

def walrus_operator():
    """
    A walrus operator allows you to assign values to a variable, within an expression, even to a variable that doesn't yet exist.
    """
    print("Walrus Operators: ")
    
    # The conventional way
    num = int(input("Enter a number"))
    print(num)

    # The Walrus way
    # print(wal := int(input())) # Requires Python 3.8+

    input("\nHit enter to continue...")

def what_indeed():
    print("Alright, but apart from the sanitation, the medicine, education, wine, public order, irrigation, roads, the fresh-water system, and public health, what have the Romans ever done for us?")

    input("\nHit enter to continue...")

    
words = ["Hello", "world", "!"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
           "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]

a = 2


if __name__ == "__main__":
    # Code to execute when run directly
    congrats("Iain", "First", "Python for Beginners")    

    print("<<<!!! End of Script !!!>>>")
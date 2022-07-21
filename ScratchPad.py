#! /usr/bin/python3

# Random Python Scratch Pad

def python_core():
    def control_structures():
        """
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
    def oop():
        """
        73.1 - Classes
        73.2 - Student Class
        74.1 - Inheritance
        74.2 - Fun with Classes
        75.1 - Magic Methods & O...
        75.2 - Bank Accounts
        76.1 - Object Lifecycle
        76.2 - ???
        77.1 - Data Hiding
        77.2 - Making a Deposit
        78.1 - Class & Static Methods
        78.2 - Static Methods
        79.1 - Properties
        79.2 - Property Values
        80.1 - A Simple Game
        80.2 - ???
        81.1 - Module 8 Quiz
        82 - Juice Maker
        """


### Module Imports ###

### Functions ###

def congrats(name, count, course):
    """
    Just for fun, way of marking milestones in my learning journey. ;)
    """
    print("Congrats:")
    
    print(f"Congrats {name}, on achieving your {count} certificate in {course}!!!")

    input("\nHit enter to continue...")

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

def simple_calculator(x, y, op):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    def floor(a, b):
        return a // b
    
    def modulus(a, b):
        return a % b

    if op == "+":
        result = add(x, y)
    elif op == "-":
        result = subtract(x, y)
    elif op == "*":
        result = multiply(x, y)
    elif op == "/":
        result = divide(x, y)
    elif op == "//":
        result = floor(x, y)
    elif op == "%":
        result = modulus(x, y)
    else:
        result = "Operator Error!!!"


    print(f"{x} {op} {y} = {result}")

def booleans(x, y):
    """
    Comparing values to determine if they are equal.
    """
    z = x == y
    print(f"{x} == {y}: {z}")

def booleans_no_match(x, y):
    """
    Comparing values to determine if the are not equal.
    """
    z = x != y
    print(f"{x} != {y}: {z}")

def comparisons(a, b):
    """
    Comparing values to determine truth.
    """
    x = a > b
    y = a == b
    z = a < b

    if x is True:
        print(f"{a} > {b}: {x}")
    if y is True:
        print(f"{a} == {b}: {y}")
    if z is True:
        print(f"{a} < {b}: {z}\n")

def greater_than_or_equal_to(a, b):
    """
    Comparing values to determine if greater than or equal to.
    """
    x = a <= b
    y = a >= b

    if x is True:
        print(f"{a} <= {b}: {x}")
    if y is True:
        print(f"{a} >= {b}: {y}")

def nested_if(x, y, z):
    num = x
    if num > y:
        print(f"{num} is greater than {y}")
        if num <= z:
            print(f"{num} is between {y} and {z}")

def if_else(num1, num2):
    x = num1
    if x == num2:
        print("Yes")
    else:
        print("No")

def the_club(age, name):
    """
    Code coach: Determine if a person is old enough for admittance to the club.
    """
    if age >= 18:
        print(f"Welcome {name}")
    else:
        print("sorry")

def numbers(x):
    num = x
    if num == 1:
        print("One")
    else:
        if num == 2:
            print("Two")
        else:
            if num == 3:
                print("Three")
            else:
                print("Something else")

def numbers2(x):
    num = x
    if num == 1:
        print("One")
    elif num == 2:
        print("Two")
    elif num == 3:
        print("Three")
    else:
        print("Something else")


if __name__ == "__main__":
    # Code to execute when run directly
    congrats("Iain", "First", "Python for Beginners")

    print("\nNumbers:\n")
    numbers2(3)
    numbers2(1)
    numbers2(9)
    numbers2(2)
    input("\nHit Enter to continue...")

    print("\nNumbers:\n")
    numbers(3)
    numbers(1)
    numbers(9)
    numbers(2)
    input("\nHit Enter to continue...")

    print("\nThe Club:\n")
    the_club(24, "James")
    input("\nHit Enter to continue...")

    print("\nelse Statements:\n")
    if_else(4, 5)
    if_else(9, 9)
    input("\nHit Enter to continue...")

    print("\nNested if Statements:\n")
    nested_if(12, 5, 47)
    input("\nHit Enter to continue...")

    print("\nGreater Than or Equal to? :\n")
    greater_than_or_equal_to(7, 8)
    greater_than_or_equal_to(9, 9.0)
    print("Annie" > "Andy")
    input("\nHit Enter to continue...")

    print("\nComparison:\n")
    comparisons(7, 5)
    comparisons(10, 10)
    input("\nHit Enter to continue...")

    print("\nBooleans not equal:\n")
    booleans_no_match(1, 1)
    booleans_no_match("seven", "eleven")
    booleans_no_match(2, 10)
    input("\nHit Enter to continue...")

    print("\nBooleans:\n")
    my_boolean = True
    print(my_boolean)
    booleans(2, 3)
    booleans("hello", "hello")
    input("\nHit Enter to continue...")
    
    print("<<<!!! End of Script !!!>>>")
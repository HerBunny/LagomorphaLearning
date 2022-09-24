#! /usr/bin/python3

# Random Python Scratch Pad

def python_core():
    def control_structures():
        """
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
    def Regular_Expressions():
        """
        83.1 - Regular Expressions
        83.2 - Contacts Database
        84.1 - Simple Metacharacters
        84.2 - Starts with Ends With
        85.1 - Character Classes
        85.2 - Online Shop Search
        86.1 - More Metacharacters
        86.2 - Authentication!
        87.1 - Groups
        88.1 - Special Sequences
        88.2 - Social Media Pro
        89.1 - Email Extraction
        90.1 - Module 9 Quiz
        91 - Phone Number Validator Coding Project
        """
    def Pythonicness_and_Packaging():
        """
        92.1 - The Zen of Python
        93.1 - PEP
        94.1 - More on Function Arg...
        94.2 - Infinite Sum
        95.1 - Tuple Unpacking
        96.1 - Ternary Operator
        96.2 - Give Me My Money
        97.1 - More on else Statements
        97.2 - Too Young to Ride
        98.1 - __main__
        99.1 - Major 3rd-Party libr...
        100.1 - Packages
        101.1 - Packaging for Users
        101.2 - ???
        102.1 Module 10 Quiz
        103 Adding Words Coding Project
        """

### Module Imports ###

import numpy as np

### Functions ###

def congrats(name, count, course):
    """
    Just for fun, way of marking milestones in my learning journey. ;)
    """
    print("Congrats:")
    
    print(f"Congrats {name}, on achieving your {count} certificate in {course}!!!")

    input("\nHit enter to continue...")

def tag():
    print("     👨‍💻      🐇")
    print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    print("⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛")
    print("⬛⬛⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛")
    print("⬛⬛⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛")
    print("⬛⬛⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛")
    print("⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛")
    print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")

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

def usingAll(num_list):
    if all([i > 10 for i in num_list]):
        print("True")
    else:
        print("False")

def boolean_and():
    print(1 == 1 and 2 == 2)
    # True
    print(1 == 1 and 2 == 3)
    # False
    print(1 != 1 and 2 == 2)
    # False
    print(2 < 1 and 3 > 6)
    # False

def humidity(percent):
    if percent >= 40 and percent <= 60:
        print("norm")

    input("\nHit enter to continue...\n")

def boolean_or():
    """
    """
    print(1 == 1 or 2 == 2)
    # True
    print(1 == 1 or 2 == 3)
    # True
    print(1 != 1 or 2 == 2)
    # True
    print(2 < 1 or 3 > 6)
    # False    

    input("\nHit enter to continue...\n")

def boolean_not():
    """
    """
    print(not 1 == 1)
    # False
    print(not 1 > 7)
    # True

    input("\nHit enter to continue...\n")

def true_or_false():
    print(False == False or True)
    # True
    print(False == (False or True))
    # False
    print((False == False) or True)
    # True    

    input("\nHit enter to continue...\n")

def grade_check(grade):
    if (grade >= 70 and grade <= 100):
        print("Passed!")
    else:
        print("Failed")

def lists():
    """
    """
    str = "Hello world!"
    print(str[6])

    words = ["Hello", "world", "!"]
    print(words[0])
    print(words[1])
    print(words[2])

    empty_list = []
    print(empty_list)

def lists_2():
    """
    """
    number = 3
    things = ["string", 0, [1, 2, number], 4.56]
    print(things[1])
    print(things[2])
    print(things[2][2]) # third element, in third element of list   
    
def matrices():
    """
    """
    m = [
        [1, 2, 3],
        [4, 5, 6]
        ]

    print(m[1][2]) # Third element in second row

def my_arrays():
    """
    Playing with NumPy Arrays.
    """
    d = np.full((2,2), 9, dtype = np.float32)
    print(d)
    input("\nHit enter to continue...\n")

    a = np.ones((3, 2))
    print(a)
    input("\nHit enter to continue...\n")


    b = np.zeros((3, 4))
    print(b)
    input("\nHit enter to continue...\n")

    c = np.random.random(3)
    print(c)
    input("\nHit enter to continue...\n")

    d = np.full((2, 2), 12)
    print(d)
    input("\nHit enter to continue...\n")

    my_arr = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8]
        ])

    print(my_arr)

    print(my_arr[1, 2])

    print(my_arr.ndim)

    print(my_arr.shape)

    print(my_arr.size)

    print(type(my_arr))

def arr_creating_a_sequence():
    a = np.arange(0, 10, 2)
    print(a)
    input("\nHit enter to continue...\n")

    b = np.arange(6)
    print(b)
    input("\nHit enter to continue...\n")

    c = np.linspace(0, 10, 6)
    print(c)
    input("\nHit enter to continue...\n")

def changing_array_size_and_shape():
    a = np.arange(10)
    print(a.shape)
    input("\nHit enter to continue...\n")

    print(a)
    input("\nHit enter to continue...\n")

    a.resize(2, 5)
    print(a.shape)
    input("\nHit enter to continue...\n")

    print(a)
    input("\nHit enter to continue...\n")

    b = np.array([[1, 2, 3], [4, 5, 6]])
    print(b)
    input("\nHit enter to continue...\n")

    print(b.reshape(3, 2))
    input("\nHit enter to continue...\n")

    print(b.shape)
    input("\nHit enter to continue...\n")

    print(b.ravel())
    input("\nHit enter to continue...\n")

    print(b.shape)
    input("\nHit enter to continue...\n")

    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a.transpose())
    input("\nHit enter to continue...\n")

def array_slicing():
    x = np.arange(8)

    y = x[0:4]
    print(y)
    input("\nHit enter to continue...\n")

    z = x[6:]
    print(z)
    input("\nHit enter to continue...\n")

    print(x[:5])
    input("\nHit enter to continue...\n")

    z[1] = 100
    print(x)
    input("\nHit enter to continue...\n")

    a = np.array([
        [10, 11, 12, 13],
        [20, 22, 23, 25]
        ])

    print(a[0:1, 1]) # 2nd element of first two rows
    input("\nHit enter to continue...\n")

    print(a[..., 1]) # 2nd element of each row
    input("\nHit enter to continue...\n")

    print(a[:, 3])
    input("\nHit enter to continue...\n")

def arithmetic():
    x = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8]
        ])

    y = np.array([
        [9, 10, 11, 12],
        [13, 14, 15, 16]
        ])

    print(np.add(x, y))
    input("\nHit enter to continue...\n")

    print(np.remainder(y, x))
    input("\nHit enter to continue...\n")

    print(x**2)
    input("\nHit enter to continue...\n")

    print(y - x)
    input("\nHit enter to continue...\n")

    print(x < 5)
    input("\nHit enter to continue...\n")

def elementwise():
    x = np.array([[1, 2], [3, 4]])
    print(np.exp(x)) # Exponential
    input("\nHit enter to continue...\n")
    print(np.sqrt(x)) # Square root
    input("\nHit enter to continue...\n")

def array_functions():
    x = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8]
        ])

    y = np.array([
        [9, 10, 11, 12],
        [13, 14, 15, 16]
        ])
    
    print(x.sum(axis = 0))
    input("\nHit enter to continue...\n")

    print(np.min(x))
    input("\nHit enter to continue...\n")

    print(x.max(axis = 1))
    input("\nHit enter to continue...\n")

    print(np.cumsum(y))
    input("\nHit enter to continue...\n")

    print(np.corrcoef(y))
    input("\nHit enter to continue...\n")

    print(y.std())
    input("\nHit enter to continue...\n")

def broadcasting():
    two_d = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8]
        ])

    one_d = np.array([[10]])

    three_d = np.ones((3, 2))

    print(np.add(two_d, one_d))
    input("\nHit enter to continue...\n")

    print(np.add(one_d, three_d))
    input("\nHit enter to continue...\n")

def dejavu():
    """
    Code coach to find if you've typed a character more than once in an input string.
    """
    str = input("Type something: ")
    print(str)
    deja = False

    for char in str:
        x = char
        if str.count(x) > 1:
            deja = True

    if deja == True:
        print("Deja Vu")
    else:
        print("Unique")
               

if __name__ == "__main__":
    # Code to execute when run directly
    congrats("Iain", "First", "Python for Beginners")

    dejavu()

    print("<<<!!! End of Script !!!>>>")
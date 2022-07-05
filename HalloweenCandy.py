# Halloween Candy

# You go trick or treating with a friend.  All, but three houses are giving away candy.  One house 
# is giving away toothbrushes and two are giving out $1 bills. Given the total number of houses 
# visited, what is the chance of pulling a dollar bill from your bag?

import math

houses = int(input("How many houses have you visited? "))

chance = math.ceil((2/houses)*100)
print(f"There is a {chance}% chance of you pulling a dollar bill, from your bag.")
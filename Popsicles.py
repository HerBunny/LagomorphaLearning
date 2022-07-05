# Popsicles

# This is a script to determine whether you should give your siblings popsicles, or eat them 
# yourself.  If there are enough to divide equally amongst your siblings, you'll give them the 
# popsicles.  If not, you'll eat them yourself.

siblings = int(input("How many siblings do you have? "))
popsicles = int(input("How many popsicles have you got? "))

if popsicles % siblings == 0:
    print("Give the popsicles to your siblings.")
else:
    print("Rather, eat them yourself.")
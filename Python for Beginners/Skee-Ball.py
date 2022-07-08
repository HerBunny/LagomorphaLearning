# Skee-Ball

# Determine if you have enough tickets to buy a squirt gun.

points = int(input())
cost = int(input())
tickets = points/12

if tickets >= cost:
    print("Buy it!")
else:
    print("Try again")

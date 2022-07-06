# Fruit Bowl

# There's a bowl on the counter, half filled with apples, half are bananas.  It takes 3 apples to 
# make a pie.  Given the number of fruit in the bowl, how many pies can be made?

fruit = int(input())

bananas = fruit/2
apples = bananas
pies = int(apples//3)

print(f"There are {bananas} bananas.")
print(f"And {apples} apples.")
print(f"You will be able to make {pies} pies.")
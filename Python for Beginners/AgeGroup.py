user_age = int(input())

# Child: 0 to 11
# Teen: 12 to 17
# Adult: 18+

if user_age <= 11:
    print("Child")
elif (user_age >= 12 and user_age <= 17):
    print("Teen")
else:
    print("Adult")


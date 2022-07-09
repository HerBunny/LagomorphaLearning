# Ticketing

# This script is used to take input on the ages of five passangers.
# Then, by using continue to skip over passangers who are younger than 3,
# It calculates the total fares for the rest of the passangers.

fares = 100 # The price per ticket
passengers = []
takings = 0

while len(passengers) < 5:
    user_input = int(input())
    passengers.append(user_input)

for passenger in passengers:
    if passenger < 3:
        continue
    takings += fares

print(takings)

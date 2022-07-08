# Paint costs

# Calculate the cost of materials needed for a paint project.

import math

colors = int(input())
canvas_and_brushes = 40.00
paint = 5.00

def calculate_total_cost(colors, paint, canvas_and_brushes):
    cost = ((paint * colors) + canvas_and_brushes)
    tax = cost * 0.1
    total = math.ceil(cost + tax)
    return total

total = calculate_total_cost(colors, paint, canvas_and_brushes)

print(total)
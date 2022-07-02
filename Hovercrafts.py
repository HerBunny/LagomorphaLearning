# Variables set to values required for passing assignment
qty_manufactured = 10
cost = 2000000
retail_price = 3000000
insurance = 1000000

# Additional variables to calculate profit and loss
sales = 0
overheads = 0
earnings = 0
profit_loss = ""


# Logic function to calculate profit and loss for the month
def calculate_sales(qty_manufactured, cost, insurance, retail_price):
    global overheads
    global earnings
    global profit_loss
    overheads = (qty_manufactured * cost) + insurance
    earnings = sales * retail_price
    if overheads > earnings:
        profit_loss = "Loss"
    if overheads == earnings:
        profit_loss = "Broke Even"
    if overheads < earnings:
        profit_loss = "Profit"


print(profit_loss) # Essential for passing the assignment

# Argentina

# Comparing whether or not it's cheaper to pay for a hat in Pesos, or Dollars, based on a set currency exchange rate.

price_ARS = int(input()) # Input the price in Pesos
price_USD = int(input()) # Input the price in Dollars
rate = 0.02 # 2 cents USD to every Peso

ARS_to_USD = price_ARS * rate
USD_to_ARS = price_USD / rate

if (ARS_to_USD < price_USD and ARS_to_USD < USD_to_ARS):
    print("Pesos")
else:
    print("Dollars")

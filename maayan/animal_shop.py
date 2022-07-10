import math
 
f = open(r"C:\Users\jbt\maayan\animals.csv")
lines = f.readlines()
lines.pop()
lines.pop()
 
companies = []
products = []
prices = []
types = []
shop = []
dog_prices = []
 
for l in lines[1:]:
    l.strip('\n')
    pair = l.split(',')
    print(pair)
    companies.append(pair[0])
    products.append(pair[1].replace(" ",""))
    prices.append(int(pair[2].replace(" ","")))
    types.append(pair[3].strip('\n').replace(" ",""))
shop.append([companies, products, prices, types])
 
max_price = max(prices)
max_item = products[prices.index(max_price)]
print(max_item)
print(types)
types
for b in shop:
    if types == "dog_food":
        dog_prices.append(types)
print(dog_prices)
 
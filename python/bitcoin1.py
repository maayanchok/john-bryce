import statistics
from statistics import mean
from statistics import median

li_bit = []
prices = []
dates = []
new_dates = []

f = open(r'C:\Users\maaya\Documents\python\btc_historical_price.csv')
bit_lines = f.readlines()
for i in (bit_lines[1:]):
    i = i.strip("\n")
    pair = i.split(",")
    li_bit.append(pair)

for b in li_bit:
    prices.append(b[1])
    dates.append(b[0])

prices = [float(i) for i in prices]
max_bit = max(prices)
avg = mean(prices)
med = median(prices)
print(max_bit, avg, med)
bid = int(input("what is your bitcoin proposition?"))

if bid < max_bit and bid > avg and bid > med:
    print("your prposition is accepted")
else:
    print("your proposition isnt accepted")

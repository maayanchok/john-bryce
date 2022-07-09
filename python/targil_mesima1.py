import statistics
from statistics import mean
from statistics import median


from numpy import index_exp

desti = []
flights = []
new = []
old_desti = []
index_desti = []
your_price = []
all_desti = []

f = open(r'C:\Users\maaya\Documents\python\flights.csv')
lines_flight = f.readlines()
lines_flight.pop()


for l in lines_flight[1:]:
    l = l.strip('\n')
    pair = l.split(',')
    flights.append(pair)
for i in flights:
    old_desti.append(i[1])
for d in old_desti:
    d = d.replace(" ","")
    desti.append(d)

your_desti = "London"
for index, a in enumerate(desti):
    if a == your_desti:
        index_desti.append(index)
for b in index_desti:
    print(flights[b])
    your_price.append(flights[b][2])

your_price = [int(c) for c in your_price]
print(your_price)
a,b = mean(your_price),median(your_price)
print(a,b)




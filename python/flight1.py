#def get_flight_num():
l1 = []
l2 = []
flight_num = []
f = open(r"C:\Users\maaya\Documents\python\flights.csv")
lines = f.readlines()

for l in lines[1:]:
    l = l.strip('\n')
    pair = l.split(',')
    for i in pair:
        l1.append(pair[0])
    print(l1)




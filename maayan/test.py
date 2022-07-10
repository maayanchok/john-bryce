import csv
with open('ages.csv', 'w', newline='') as f:
    f.write("age")
    f.write("maayan")
    f.write("Tom")
    f.write("tal")
for line in f:
	print(line, end = '')


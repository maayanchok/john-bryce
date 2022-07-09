
def op_excel(adress,col):
    l1 = []
    f = open(adress)
    lines = f.readlines()
    for l in lines[1:]:
        l = l.strip('\n')
        pair = l.split(",")
        i = 0
        # if type(i in pair) == int:
        #li.append(int(pair[col]))
        #else:
        new_row = []
        for i in col:
            new_row.append(pair[i])
        print(new_row)
        l1.append(new_row)
    print(l1)




       
    
   

# a = input("whats the name of the file?")
a = (r"C:\Users\maaya\Documents\python\flights.csv")
# b = input("which column do you want to see?")
b = [0,1]
print(op_excel(a,b))
num1 = (0,5,8,6,8,7,8,3,0,0)
num2 = (0,5,8,3,6,7,4,7,5,2)
num3 = (0,2,4,6,3,5,7,5,4,5)

def check_num(your_num):
    li_num = []
    for a in your_num:
        for i in range(0,10):
            if i == a:
                li_num.append(i)
    li_num = [str(int) for int in li_num]
    print("".join(li_num))
            
check_num(num1)
check_num(num2)
check_num(num3)

import user_to_dict_op.dict_op as op

users = {}
f = open("drivingschool.html","a")

answer = ""
while answer!="n":
    users = op.add_to_dict()
    answer = input("Do you want to add new users?  y/n ")

for di in users:
    
    f.write("<tr>")
    for title in users[0].keys():
        head = (f"<th>{title}</th>")
        f.write(head)
    f.write("</tr>")

    f.write("<tr>")
    for user in di.values():
        message= (f"<td>{user}</tr>")
        f.write(message)
    f.write("</tr>")

print("The list of users have been added ")
f.close()


b={}
n=int(input("enter no of students "))
for i  in range(n):
    x,y=map(str,input("enter student and marks ").split(" "))
    b[x]=y

while True:
    name=input("Enter the name of students whose marks u want ")
    marks=b.get(name,-1)
    if marks==-1:
        print("Student not found")
    else:
        print("the marks of ",name," are ",marks)
    opt=input("do u wanna continure(yes)(no)")
    if opt=="no":
        break


"""
for x,y in b.items():
    print(x,y)
"""
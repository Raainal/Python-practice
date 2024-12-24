a={"x":2,"y":1,"z":3}
b=[]
for i in a.values():
    b.append(i)
c=sorted(b)
print(c)
i=0
sort={}
# make a new dict with the values sorted
for x,y in a.items(): # ghar jaake kar ye galat aaya hai
    for i in range(len(a)):
            if y==c[i]:
                 i+=0
                 sort[x]=y
print (sort)

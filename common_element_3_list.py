l1=[1,2,3]
l2=[3,4,5]
l4=[2,3,4]
l3=[]
for i in l1:
    if i in l2 and i in l4:
        l3.append(i)
print(l3)

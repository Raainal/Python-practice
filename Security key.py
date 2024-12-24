a=578378923
a=str(a)
c=0
for i in a:
    if a.count(i)>1:
        c+=1
        a=a.replace(i,"")
print("security key is ",c)
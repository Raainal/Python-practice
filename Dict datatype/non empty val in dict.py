a={"x":20,"y":10,"z":30,"f":None,"r":""}
c=0
for x in a.values():
    if x==None or x=="":
        c+=1

print(len(a)-c)
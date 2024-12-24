a={"x":20,"y":10,"z":30}
b=[]
for i in a.values():
    b.append(i)
b=min(b)
print(b)
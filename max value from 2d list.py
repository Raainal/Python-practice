list=[[100,198,333,323],[122,232,221,111],[223,565,245,764]]
a=[]
print(len(list))
for i in range(len(list)):
    a.append(max(list[i]))
print(a)
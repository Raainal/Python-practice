'''
i/p aaabbbcccc
o/p  a3b3c4
'''

a="aaabbbcccccc"
b={}

for i in a:
    b[i]=a.count(i)

for x,y in b.items():
    print(x,y,sep='',end='')


'''
another method 

for i in range(len(name)):
    key=name[i]# name[0],key=b
    count=0
    for j in range(len(name)):
    if name[j]==key:
    count+=1
    b[key]=count
'''
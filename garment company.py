n=int(input())
list=[]
c=0
s=0
for i in range(n):
    a=int(input())
    list.append(a)
print()
for j in range(1,10):
    s=j*j
    if s in list:
        print(s,end=' ')
        c=c+1
print()
print(c)
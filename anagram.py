s1="listen"
s2="silent"
c1=0
c2=len(s1)
for i in s1:
    if i in s2:
        c1+=1
if c1==c2:
    print("ana")
else:
    print("not ana")

'''
another way to do it

a,b=list(s1),list(s2)
a.sort()
b.sort()
if a==b
    print("ana")
else
    print("not ana")
'''
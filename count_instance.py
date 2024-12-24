'''
i/p abababab and ab
o/p 4
'''
a="abababababab"
b="ab"
c=0
for i in a:
    if b in a:
        c+=1
print(c//2)
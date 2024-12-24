s1="the quick brown fox jumps over the lazy dog"


#ascii 97 to 122
c2=0
for i in s1:
    if ord(i)>=97 and ord(i)<=122:
        c2+=1
print(c2)
if c2==26:
    print("panagram")
else:
    print("not panagram")
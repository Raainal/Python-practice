s="amal*is*super*duper*awesome"
a,b="",""
for i in s:
    if i=="*":
        a=a+i
    else:
        b=b+i
print(a+b)
n=int(input("Enter no of numbers "))
s=[]
sum=0
for i in range(n):
    num=int(input("Enter number "))
    s.append(num)
    sum+=abs(s[i-1]-s[i])
print(sum)
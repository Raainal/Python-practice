n=int(input())
dist=[]
for i in range(n):
    dist.append(int(input()))

for i in dist:
    if i>=30 and i<=50:
        print(i,end=" ")
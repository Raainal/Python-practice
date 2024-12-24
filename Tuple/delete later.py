n = int(input())

for i in range(0, n):
    if i % 2 == 0:
        if i + 2 >= n:  
            print(i, end="")  
        else:
            print(i, end=",") 

if n % 2 == 0 and n > 0:
    print(",", n, sep="")
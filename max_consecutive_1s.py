l1=[1,1,0,1,1,1,0,1,1,1,1,0,1,1]
count1=0
count2=0
for i in l1:
    if i==1:
        count1+=1
    elif(count1>count2):
        count2=count1
        count1=0
    else:
        count1=0
print(count2)
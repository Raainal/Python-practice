mylist=list(input("enter number without spaces "))
for i in mylist:
    if mylist.count(i)==1:
        print(i)
        break

'''
find first element that is non repeating 
i/p 1232415
o/p 3
'''
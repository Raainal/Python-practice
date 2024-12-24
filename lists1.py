mylist=["prashant","Ashish","komal","ankush","ashish",77,"sandip",60.52,'akshay']
'''print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[1:8:2])

print(mylist)
mylist[0]="Akshay" #muteable proof
print(mylist)

mylist.append("amal")
mylist.append("nair")
print(mylist)
#inset object at specific place
mylist.insert(0,"sanket")
print(mylist)
#remove object from list
mylist.remove("sandip")
print(mylist)
# copy list
new_list=mylist.copy()
print(new_list)

#multidimensional list

mylist=[["prashant","Ashish"],[60.52],[440022,"yyy"]]
print(mylist)
print(mylist[0][0])

list1=["prashant","jha"]
print(list1*2)

list2=[50,25,"pras"]
print(list1+list2)

del list2[2]
#del list2         used to delete a whole list
print(list2)

list2.clear()
print(list2)

name="prashant"
#print(name)
myname=list(name)#type casting into list
#print(myname)

name="prashant"
print(name)
myname=list(name)#type casting into list
print(myname)

myname.reverse()
print(myname)
# reverse can also be done as  myname[::-1]

myname.sort() #sorts in ascending
print(myname)
# sort function only works if the list has homogeneous(same data type) values or it gives type error
myname.sort(reverse=True)
print(myname)
'''

mylist=[1,2,4,5,2,1,3,6,2]
print(mylist.count(1))
print(mylist.count(4))
print(mylist.count(2))

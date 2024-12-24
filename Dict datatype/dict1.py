'''
mydict={
    "name":"prashant",
    "proffession":"dev",
    "empid":1001
}
print(mydict)
print(type(mydict))
'''

mydict={
    101:"prashant",
    102:"dev",
    103:"mohini",
    104:"trivani",
    101:"dev",
    104:"dev",
}
print(mydict)

#with the help of key , print

a=mydict[102]
print(a)

mydict[102]="peter"
print(mydict)

# only prints the key and not the value
for x in mydict:
    print(x)

# to print only values
for x in mydict.values():
    print(x)

# print both key and value

for x,y in mydict.items():
    print(x,y)

#how to add key and value pair in an already existing dictionary

mydict["mobile no"]=123456789
print(mydict)

#pop is used to remove a key and value pair in python
mydict.pop(101)
print(mydict)

#to create clone
newdict=mydict.copy()
print(newdict)


def msg():
    uname=input("enter uname")
    passw=input("enter pass")
    if uname==passw:
        print("in")
    else:
        print("not in")
#msg()

'''
types of arguement
-------------------------------------------------------------------------------------------
positional arguement
keyword argument
default argument
variable length argument/ variable number of arguement
unknown arguement
'''

#positional arguement
def info(fname,lname):
    print("first name is ",fname)
    print("last name is ",lname)
#info("sachin","tendulkar")

#positional passin in correct order
def add(n1,n2):
    return n1+n2
res=add(2,3)
print(res)
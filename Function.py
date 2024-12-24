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
#print(res)

def math(n1,n2):
    r=n1+n2
    m=n1*n2
    n=n1/n2
    return r,m,n
res=math(2,3)
#print(res)

def func(name):
    for i in name:
        print(i)
name_of=["amal","dharshu","shib","bitch"]
#print(func(name_of))

#def name(*name):
    #print(name)
#name("ashish","prashant","tushar",1001)
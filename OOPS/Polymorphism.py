'''class arithmatic:
    def add(self, a):
        print(a) 
    def add(self, a, b):
        print(a + b)
    def add(self, a, b, c):
        print(a + b + c)

obj=arithmatic()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)'''

'''
class arithmatic:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None:
            print(a+b)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)
        else:
            print("enter atleast two values")
obj=arithmatic()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)'''

class arithmatic:
    def __init__(self):
        print("there is no arguement")
    def __init__(self,a):
        print("one arguement",a)
    def __init__(self,a,b):
        print("two arguement",a,b)
obj=arithmatic()
obj=arithmatic(10)
obj=arithmatic(10,20)
#pythin supports operator overloading by using magic methods
#magic methods are the special methods which have double underscore at the beginning and end of their names
#magic methods are also called dunder methods
#magic methods are used to define the behaviour of objects
#magic methods are automatically called when a specific event occurs
#magic methods are used for operator overloading



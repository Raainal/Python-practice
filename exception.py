a=int(input("enter first val "))
b=int(input("enter 2nd val "))
try:
    a=int(input("enter first val "))
    b=int(input("enter 2nd val "))
    c=a/b
    print(c)
except ZeroDivisionError as message:
    print("error zero",message)
except ValueError as message:
    print("error val",message)

print("continue")
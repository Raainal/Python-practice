'''
mytuple=("prashant","ashish","rahul","sandip","komal",23,3.15,77,"sandip")
print(mytuple)
print(type(mytuple))
''
mytuple(2)="sunil"
print(mytuple)

its not possible to add values or anything to tuple

do add delete sort clear or any operation in tuple 
you need to typecast it to list
list(mytuple)
and then do operations and then typecast back to tuple
tuple(mylist)
''

# function to find length of tuple   if there is no value in tuple then it will output 0
print(mytuple.__len__())
# Define a tuple with mixed data types
mytuple = ("prashant", "ashish", "rahul", "sandip", "komal", 23, 3.15, 77, "sandip")

# Print the tuple
print("Original Tuple:", mytuple)

# Print the data type of the tuple
print("Data Type of mytuple:", type(mytuple))

# Attempt to modify a tuple (this will raise an error)
try:
    mytuple[2] = "sunil"
except TypeError as e:
    print("Error:", e)

# Convert the tuple to a list to perform operations
mylist = list(mytuple)

# Print the list
print("Converted List:", mylist)

# Perform operations on the list
mylist.append("new_element")
mylist.sort()

# Print the modified list
print("Modified List:", mylist)

# Convert the list back to a tuple
mytuple = tuple(mylist)

# Print the modified tuple
print("Modified Tuple:", mytuple)

# Function to find the length of a tuple
def get_tuple_length(mytuple):
    return mytuple.__len__()

# Print the length of the tuple
print("Length of mytuple:", get_tuple_length(mytuple))

# Define two tuples
a = ('a', 'b')
b = ('a', 'b')

# Compare the tuples
print("Are a and b equal?", a == b)
a='a','b'
b=('a','b')

print(a==b)
'''
l=[1,2,3]
tup=('python')*(l.__len__()-l[::-1][0])
print(tup)
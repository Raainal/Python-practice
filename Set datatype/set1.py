myset={1,2,"sanjay",4.5,"amal"}

print(myset)
print(type(myset))
print("--------------------------------------")
myset.add(60) # adds the value at random places in the set
print(myset)
print("--------------------------------------")
myset.discard(60) #deletes the selected value from the set
print(myset)
print("--------------------------------------")
yset={"amal","nair",4.5}

print(myset.union(yset)) # union of 2 sets
print("--------------------------------------")

print(myset.intersection(yset)) # intersection of 2 sets
print("--------------------------------------")
print(myset.difference(yset)) # shows whats different in both set
print("--------------------------------------")
print(myset.clear()) # clears the whole set
#Sets in python

set = { 1,2,3,4,"hello","world",5.99,"suraj",2}

print(set)
print(type(set))
print(len(set))




collection = set()  # empty set; syntax

print(type(collection))



print("\n")
collection = set()
collection.add(1)
collection.add(2)
collection.add("Suraj")
collection.add(2)
collection.add((1,2,3))


print(collection)
collection.remove("Suraj")
print(type(collection))
print(collection)



print("\n")
collection = set()
collection.add(1)
collection.add(2)
collection.add("Suraj")
collection.add(2)
collection.add((1,2,3))

print(len(collection))
print(collection)
collection.clear()
print(type(collection))
print(len(collection))


print("\n")
collection = {"hello","Suraj","world","python"}
print(collection.pop())
print(collection.pop())
print(collection.pop())
print(collection.pop())



print("\n")
set1 = { 1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1)
print(set2)


print("\n")
set1 = { 1,2,3}
set2 = {3,4,5}
print(set1.intersection(set2))
print(set1)
print(set2)



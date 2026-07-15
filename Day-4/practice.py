#Practice dictionary and sets

#Store following word meanings in a python dictionary : 

# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal”


dict = {
     "cat" : "a small animal",
     "table" : ["a piece of furniture","list of facts & figures"]
    
}

print(dict)


print("\n")
# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# ”python”, “java”, “C++”, “python”, “javascript”,
# “java”, “python”, “java”, “C++”, “C

set = {"python","java","C++","python","javascript",
       "java","python","java","C++","C"}

print(set)
print(len(set))


print("\n")
# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
Dict = {}
print(Dict)

x = int(input("Enter Your Maths Marks : "))
Dict.update({"Maths" : x})

y = int(input("Enter Your Physics Marks : "))
Dict.update({"Physics" : y})

z = int(input("Enter Your English Marks : "))
Dict.update({"English" : z})

print(Dict)




print("\n")
# Figure out a way to store 9 & 9.0 as separate values in the set. 
# (You can take help of built-in data types)

values = { 9 , 9.0}
print(values)

values = { "9" , 9.0}
print(values)

values = { 9 , "9.0"}
print(values)

values= {
    ("float", 9.0),
    ("int", 9),
}
print(values)



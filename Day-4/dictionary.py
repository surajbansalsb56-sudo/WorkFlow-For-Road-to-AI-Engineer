#dictionaries in python

info = {
    "Name": "Suraj Bansal",
    "Dob"  : " 1 November 2006",
    "Age" : 20,
    "Is_Adult" : True,
    "learning" : "Python",
    "Subjects" : ["Python","Java","C"],
    "topics" : ("dictionary","sets",),
    "Marks" : 99.5,
    "Cgpa" : [8.5,9.0,9.5],
}

print(info)
print(type(info))
print(info["Name"])
print(info["Subjects"])
print(info["Dob"])

info["Age"] = 19
info["Name"] = "Suraj"  #overwrite
info["surname"] = "bansal"
print(info)


null_dict = {}
null_dict["name"] = "suraj"
print(null_dict)



# Nested Dictionary
student = {
    "Name" : "Suraj",
    "Score" : {
        "Maths" : 98,
        "Phy" : 95,
        "Che" : 99,
    }
}

print(student)
print(student["Score"])
print(student["Score"]["Maths"])
student["Score"]["English"] = 95
print(student)


print("\n")

student = {
    "Name" : "Suraj",
    "Score" : {
        "Maths" : 98,
        "Phy" : 95,
        "Che" : 99,
    }
}
print(student.keys())
print(len(list(student.keys())))
print(list(student.keys()))
print(len(student))



print("\n")
student = {
    "Name" : "Suraj",
    "Score" : {
        "Maths" : 98,
        "Phy" : 95,
        "Che" : 99,
    }
}
print(student.values())
print(list(student.values()))


print("\n")

student = {
    "Name" : "Suraj",
    "Score" : {
        "Maths" : 98,
        "Phy" : 95,
        "Che" : 99,
    }
}
print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])


print("\n")
student = {
    "Name" : "Suraj",
    "Score" : {
        "Maths" : 98,
        "Phy" : 95,
        "Che" : 99,
    }
}
print(student["Name"])     #error
print(student.get("Name"))   #no error --> None


print("\n")
student = {
    "Name" : "Suraj",
    "Score" : {
        "Maths" : 98,
        "Phy" : 95,
        "Che" : 99,
    }
}

new_dict = { "Name" : "Suraj Bansal", "age" : 19, "City": "Delhi"}
student.update(new_dict)
print(student)



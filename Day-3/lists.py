
#Lists  #list --> mutable , #strings --> immutable



marks = [66.2 , 94.5 , 75.5 ,82.7 , 62.6]
print(marks)
print(type(marks))
print(marks[2])
print(marks[4])
print(len(marks))


print("\n")
students = ["karan" , 85.5 , 19, "China Gate"]
print(students[0])
students[0] = "arjun"
print(students)


print("\n")
marks = [ 80, 85, 90, 95, 100]
print(marks[1 : 4])
print(marks[ : 4])
print(marks[1 : ])
print(marks[-3 : -1])



print("\n")
list = [ 1,5,3,7]
list.append(9)
print(list)
list.sort()
print(list)
list.sort(reverse =True)
print(list)




print("\n")
list = [ "apple","orange","banana","litchi"]
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)


print("\n")
list = [ "apple","orange","banana","litchi"]
print(list)
list.reverse()
print(list)



print("\n")
list = [ 7,5,9,1,3]
print(list)
list.insert(2,2)
print(list)



print("\n")

list = [1,2,3,2,1,4,5,3]
print(list)
list.remove(2)
print(list)

list = [1,2,3,2,1,4,5,3]
list.remove(5)
print(list)


list = [1,2,3,2,1,4,5,3]
list.pop(4)
print(list)

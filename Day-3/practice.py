
#Let's Practice

#WAP to ask the user to enter names of their 3 favourite movies and store them in a list .
print("\n")

movie1 = input(" Enter your first movie : ")
movie2 = input(" Enter your second movie : ")
movie3 = input(" Enter your third movie : ")

movies = [ movie1 , movie2 , movie3]
print(movies)


#WAP to check if a list contains a palindrome of elements.(Hint : use copy() method)
#[1,2,3,2,1]        [1,"abc","abc",1]

list1 = [ 1,2,3,2,1]

list = list1.copy()
list.reverse()

if(list == list1):
  print("palindrome")
else:
  print("Not palindrome")


list2 = [ 1,"abc","abc",1]
list = list2.copy()
list.reverse()

if(list == list2):
  print("palindrome")
else:
  print("Not palindrome")



list3 = [ 1,"suraj","suraj",2]
list = list3.copy()
list.reverse()

if(list == list3):
  print("palindrome")
else:
  print("Not palindrome")



print("\n")
#WAP to count the number of students with the "A" grade in the following tuple.
#    ["C","D","A","A","B","B","A"]

#Store the above values in a list and sort them from "A" to "D".


tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))
print(type(tup))


list =  ["C","D","A","A","B","B","A"]
list.sort()
print(list)
print(type(list))
#conditional statements

light = "red"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
else:
    print("This is not valid colour")

print("End of Code")


num = 1

if(num>2):
    print("greater than 2")
if(num>3):
    print("greater than 3")
elif(num>=1):
    print("greater than or equal to 1")
else:
    print("Invalid input")



age = int(input("Enter your age:"))
print("You entered:", age)

if(age>=18):
  print("You are eligible for voting")   #indentation
else:
  print("You are not eligible for voting")

print("Thank You")





marks= int(input("Enter your marks :"))
print("Your entered marks is :", marks)

if(marks>=90):
  print("grade : A")
  print("Outstanding")
elif(marks>=80 and marks<90):
  print("grade : B")
  print("Excellent")
elif(marks>=70 and marks<80):
  print("grade : C")
  print("Good")
else:
   print("grade :D")
   print("Poor")




age = 34
if(age >= 18):
   print("can drive")
else:
   print("Cannot drive")

   


#nesting

age = 95
if(age >= 18):
   if(age >=80):
    print("cannot drive")
   else:
      print("can drive")
else:
   print("Cannot drive")   


   
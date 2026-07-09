#practice-Strings
#WAP to input user's first name and print its length

Name =input("Enter Your Name:")
print(Name)
print("Length of your name is ",len(Name))



#WAP to find the occurence of '$' in a String.

str = " The price of mango,banana,papaya,orange is $4,$8,$12,$60"
print(str.count("$"))



#Practice-Conditional_Operators

#WAP to check if a number entered by user is odd or even.

num = int(input("Enter your number:"))
print("You entered :",num)

if(num%2==0):
  print("Your Number is Even")
else:
  print("Your Number is Odd")




#WAP to find the greatest number in amoung 3 entered by user.

num1 = int(input("Enter your First Number :"))

num2 = int(input("Enter your Second Number :"))

num3 = int(input("Enter Your Third Number :"))

if(num1>num2 and num1>num3):
  print("Your First Number is Greatest",num1)
elif(num2>num3 and num>num1):
  print("Your Second Number is Greatest",num2)
else:
  print("Your Third Number is Greatest",num3)





#WAP to find the greatest number in amoung 4 entered by user.

a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))
d = int(input("Enter 4th number :"))

if(a>b and a>c and a>d):
  print("Your 1st number is greatest:",a)
elif(b>c and b>d):
  print("Your 2nd number is:",b)
elif(c>d):
  print("Your 3rd number is greatest:",c)
else:
  print("Your 4th number is greatest:",d)





#WAP to check if a number is multiple of 7 or not.

num = int(input("Enter your number:"))
print("You Entered :",num)

if(num%7==0):
  print("Your Number is Multiple of 7")
else:
  print("Your Number is Not Multiple of 7 ")

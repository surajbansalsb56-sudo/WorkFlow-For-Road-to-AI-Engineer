

#Arithmetic Operations
a = 10
b = 2
sum = a  + b
diff = a - b
product = a * b
division = a / b
module = a % b # remainder
power = a ** b # a^b

print(sum)
print(diff)
print(product)
print(division)
print(module)
print(power)


print("Sum :", sum , "Diff :", diff , "Product :", product ,"Division :", division, "Module :", module, "Power :",  power)




#relational operators
x  = 20
b = 10
print ( x == b) # equal to
print ( x != b) # not equal to
print ( x > b ) # greater than
print ( x < b ) # Less than
print ( x >= b) # greater or equal to
print ( x <= b) # Less than or equal to








#Assignment Operators
num = 10

num += 5
print(num)

num *= 2
print(num)

num -= 8
print(num)

num //= 3
print(num)

num %= 4
print(num)





# Assignment Operators


num1 = 15
num1 += 10 # num1 + 10 = 25
num2 = 20
num2 -=5 # num2 - 5 = 15
num3 = 30
num3 *= 2 # num3 * 2 = 60
num4 = 60
num4 /= 3 # num4 / 3 = 20.0
num5 = 20
num5 %= 3 # num5 % 3 = 2.0
num6 = 2
num6 **= 2 # num6 ** 2 = 4.0


print("num1:", num1)
print("num2:",num2)
print("num3:",num3)
print("num4:", num4)
print("num5:",num5)
print("num6:", num6)




# Logical operators are used to Boolean values and expressions. They allow you to combine multiple conditions and make decisions based on those conditions. The most common logical operators are:


# and: Returns True if both statements are true
# or: Returns True if one of the statements is true
# not: Returns True if the statement is false

print ("Logical Operators in Python")

a = 30
b = 20

print( not False) # Output : True
print ( not True) #Output : False

print ( not a > b) # Output : False
print ( not a < b) # Output : True

print ( a > b and a > 50) # Output : False
print ( a > b and a < 50) # Output = True

print ( a  > 40 or b < 10 ) # Output = False
print( a > 40 or b< 40 ) # Output = True








print ("and operator:")
x = 5
y = 10
print (x > 0 and y < 20)

print ("or operator:")
print (x > 0 or y < 5)

print ("not operator:")
print (not(x > 0 and y < 20))




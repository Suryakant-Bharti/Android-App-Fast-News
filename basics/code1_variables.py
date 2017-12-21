# This is a single line comment

'''
This
is
a
Multiline
comment
'''

# Variable Types

a = 10			# 10 is an Integer value (numbers without decimal)
b = 25.78		# 25.78 is a Float value (numbers with decimal)
c = 'John'		# John is a String value (one or more characters)
d = "Tom"		# Tom is also String value (one or more characters)

print (a)
print (b)
print (c)
print (d)

# Updating values of variables

a = 320
print (a)

a = -999
print (a)

# Assigning single value to multiple variables

x = y = z = 50  

print (x,y,z)

# Assigning multiple values to multiple variables:

p,q,r = 5,10,15  

print ('Value of p = ', p)
print ('Value of q = ', q)
print ('Value of r = ', r)

# Swaping values of 2 variables

p,q = q,p

print ('New Value of p = ', p, 'and q = ', q)

# Difference between a Number and String

num1 = 200
num2 = 300

numAdd = num1 + num2

print(numAdd)

str1 = '200'
str2 = '300'

strAdd = str1 + str2

print(strAdd)

# Creating Single-Line and Multi-Line String

string1 = 'I am a single line string'

string2 = 'I am a \
multiple line \
string. \
I can keep going \
and going \
and going... blah blah blah!!!'

string3 = '''I am also also
a multiline string'''

print(string1)
print(string2)
print(string3)

# Boolean variables in Pyhton - True and False keywords

val1 = False
val2 = True

print(val1, val2)

# None keyword - A variable with no value

int1 = 600
int2 = None

print(int1,int2)

# Basic Input/Output

name = input("What's your name? ")

print("Nice to meet you ", name, "!")

age = input("Your age? ")

print("So, you are already ", age, " years old, ", name, "!")
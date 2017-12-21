# Basic String Operations
print()
print('----- STRING BASIC OPERATIONS -----')

str1 = 'Bangalore-'
str2 = 'India'
str3 = 'I am a very very long String mango banana apple orange'

print('str1 =',str1)

print('str1 + str2 =',str1 + str2)

print('str1 * 3 =',str1 * 3)

print('str1[7] =',str1[7])

print('str1[0:4] =',str1[0:4])

print('str3[28:34] =',str3[28:34])

# Lists and List Operationa
print()
print('----- LISTS BASIC OPERATIONS -----')

list1 = [55,0,-7,99,4]
print('list1 =',list1)

list2 = ['John',26,15516.78,'Brazil']  
print('list2 =',list2)

list3 = list1 + list2
print('list1 + list2 =',list3)

list4 = list2 * 2
print('list2 * 2 =',list4)

name = list2[0]
country = list2[3]

print('name =',name,'country =',country)

print('age =',list2[1],'salary =',list2[2])

print('Information without country = ',list2[1:4])

list2[3] = 'Australia'
print('Information after country value modification = ',list2)

# Membership Operators
print()
print('----- MEMBERSHIP OPERATIONS -----')

a=10  
b=25  
c=10

list1 = [10,20,30,40,50]
list2 = [10,20,30,40,50]
list3 = [10,20,35,40,50]

print('Is 10 present in the list =',a in list1)
print('Is 15 present in the list =',15 in list1)
print('Is 25 present in the list =',b in list1)

print()

print('Is 10 not present in the list =',a not in list1)
print('Is 15 not present in the list =',15 not in list1) 
print('Is 25 not present in the list =',b not in list1) 

# Identity Operators
print()
print('----- MEMBERSHIP OPERATIONS -----')

print('a == c -->',a == c)
print('a is c -->',a is c)

print('a == b -->',a == b)
print('a is b -->',a is b)

print()

print('list1 == list2 -->',list1 == list2)
print('list1 is list2 -->',list1 is list2)

print('list1 == list3 -->',list1 == list3)
print('list1 is list3 -->',list1 is list3)
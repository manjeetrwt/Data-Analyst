                                #TYPES OF OPERATORS


#Arithmetic operators + - * / % **    numeric operations

x = 5
y = 2
print("The operators are x + y is ",x +y)       #addition
print("The operators are x + y is ",x -y)       #subtract
print("The operators are x + y is ",x *y)   #multiply
print("The operators are x + y is ",x /y)   #divide
print("The operators are x + y is ",x %y) #Remainder
print("The operators are x + y is ",x **y)      #power


#Assignement operators = += -= /= %= **=
a =2
b=4

a=b
print(a)

a +=b
print(a)

a-=b
print(a)

a/=b
print(a)

a%=b
print(a)

a**=b
print(a)


#Comparison operators  == != < > <= >= 
m=2
n=2
print(m==n)
print(m!=n)
print(m<n)
print(m>n)
print(m>=n)
print(m<=n)


#Logical operators  and or not
age=20
name='m'
print((name =='m') and (age>18))        #and 
print((name =='m') and (age>18))        #Not 
print((name =='m') or (age>18))        #or

if (name =='m') and (age>18):           #and with if condition
    print("Welocome to new journey")



#Membership operators     used to test if a sequence is present in an object or not
L=[1,2,4,5,6,78,55]
M=4
print(M in L)
print(M not in L)








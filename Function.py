#FUNCTION

# def DoSomething ():           #Syntax of function in python           
#     value = 1
#     return value

                                                        #Calling with the parameter here 
def my_name(name):
    print("Hello my name is",name)

my_name("manjeet")




def addition(a,b,c):        #Arithematic performed with return statement
    return a+b+c

result=addition(1,2,3)
print(result)



                                #LAMDA FUNCTIO  TO WRITE HUGE LINE OF CODE IN A SINGLE LINE 
#function  #lamda #parameters #block of code 
add= lambda a,b,c: print(a+b+c)
add(2,3,4)      #function calling




                                #MAP FUNCTION TO PASS MULTIPLE FUCTION 
nums=[1,2,3,4,5,6,7,8,9,10]                 #list
def sq(n):                                     #Function
    return n*n
square = map(sq,nums)               #map function calling       var=map fucntion(function name,list of values)
print(list(square))                 #printing the values in the form of list which is stored in a variable called square


                                            #ZIP FUNCTION
NAMES=["manjeet","ritesh","abhishek"]                           #To work with multiple data types together
ID=[1,2,3]
mapped=zip(NAMES,ID)
print(list(mapped))
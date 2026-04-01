                                                    #TYPES OF LOOPS IN PYTHON - FOR LOOP AND WHILE LOOP
#Loops are iterabkle in these data types - tuple list dictionary and string also because it is sequence form (sequence of character with some index)


list=[1,2,34,4,5,6,7,8,9,0,1]
for x in list:
    print(x)


                                                    #Break and continue 
print("This part is for break statement")
num=[1,2,3,10,4,5,6,7,8,9,10,10]
for x in num:
    if x==10:
        break
    print(x)

print("This part is for continue")
for i in num:
    if i ==10:
        continue
    print(i)




                                                    #While loop
num=1
while num<=10:
    print(num)
    num+=1


number=1
while number<6:
    print(number)
    if number == 4:
        break
    number+=1


Number=0                                    
while Number<20:
    Number+=1
    if Number==11:
        continue
    print(Number)


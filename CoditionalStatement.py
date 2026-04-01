                #Conditional statements
#if else elif
a,b=3,300
if a>18:                        #if
    print("can drive")


if a>b:
    print("Not greater than b")             #if else
else:
    print("bigger than b")

aman,rathod=90,90
if aman< 33:                            #if elif
    print("pass")
elif aman==rathod:
    print("both are equal")


aman,rathod=88,90
if aman< 33:
    print("pass")
elif aman==rathod:
    print("both are equal")             #if elif else
else:
    print("not equal")


if aman>rathod:
    print("aman is higher")
    if rathod<aman:
        print("rathood is high")                # if if else else nested condition
    else:
        print("both are equal")
else:
    print("Something went wrong")
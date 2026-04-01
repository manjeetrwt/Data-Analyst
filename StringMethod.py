            #String and its methods returns new value doesnt affect original
# capitalize
# isalpha
# isnumeric
# isupper
# split
# title
# strip
# replace


Str="hello my name is manjeet and im here to learn string here thanks."


#Capitalize
new_cap=Str.capitalize()
print(new_cap)

#Isaplha
alphastr="hellomanjeet"
print(alphastr.isalpha())

#Isnumeric
numstr="12345"
print(numstr.isnumeric())

#Isupper
upstr="HelloBhai"
print(upstr.isupper())

#split
splitstr="Hello bhai kaisa hai"
print(splitstr.split())

#Title
Titstr="hello bhai kaisa hai"
print(Titstr.title())


#strip/trim
TriStr="  Hello  "
print(TriStr.strip())


#Replace

Restr="hello manjeet bisht"
print(Restr.replace("bisht","rawat"))




#Count
Cntstr="Hello manjeet manjeet"
print(Cntstr.count("manjeet"))



#Find
Fstr="Hello manjeet"
print(Fstr.find("manjeet"))         # -1 if not found result

#index 
inde="Hello manjeet"
print(inde.index("manjeet"))                #priority


#Join 
names=['manjeet','gmail.com']
joined="@".join(names)
print(joined)

#starts with and ends with
Ex="Manjeet."
print(Ex.startswith("M"))
print(Ex.endswith("."))







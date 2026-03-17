                    #List indexing 0 to n left to right and in the right to left -1 to -n

#append  insert pop remove reverse sort index count

L=[1,2,3,4,5,6,7,8,8,89,7,7,6,67,6,5,6,5,6]

#Append in the end it will be get added in list
L.append('manjeet')
print(L)

#remove
L.remove('manjeet')
print(L)

#Sort  it will sort the list only one type of data set present in list if numeric is it will sort numeric based in the other hand alphabetical sort
L.sort()
print(L)

#Reverse
L.reverse()
print(L)

#Pop
L.pop(4)          #position 0 to n
print(L)

#insert  .insert(posi,element)
L.insert(2,"rawat")
print(L)

#index it will return the position of the element
L.index('rawat')

#Extent
L1=[2,3,4,5,6,7,8,8,5]
L.extend(L1)
print(L)

#Count the element
print("The number of times 8 is coming ",L.count(8))

#copy  for the trial error to create a dummy of our list
L3=L.copy()
print(L3)

#clear
L3.clear()
print(L3)

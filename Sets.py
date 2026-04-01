#Sets in python
#{ } curly brackets - NO diplicate values 
# -not change -only instance will be changed(temporary purpose)


                            #METHODS IN SETS

#is super set
#copy
#clear and add
#issubset
#difference
#instersection
#union
#remove
#discard


sets={1,2,3,4,6,7,888,90}


#Add
sets.add(100)
print(sets)             #randomness

#Pop
sets.pop()
print(sets)             #random pop

#remove
sets.remove(100)            #specific
print(sets)

#difference x-y
x={1,55,4,3,32,2,3,22,888}
y={1,55,4,3,32,3,888,22}
print(x.difference(y))


#intersections
print(x.intersection(y))   #Common things

#union
print(x.union(y))           #gives the common thing also with unique vales and random


#update
print(x.update(y))
print(y)

x |=y
print(x)
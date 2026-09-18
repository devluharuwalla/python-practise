fruit = "apple"
print(fruit)

fruits = ["apple", "orange", "Banana", "coconut"] #list of fruit named fruits

print(fruits)

#to access element, use index value starting from 0

print(fruits[0])

print(fruits[3])

print(fruits[0:3])


print(fruits[0::3])

print(fruits[::-1])

for x in fruits:
    print(x)

#dir(fruits)) gives attributes

#help(fruits) #gives everything you can do with list, have to printtho

print(len(fruits))

print("pineapple" in fruits) # check if pineapple in list fruits

fruits[0] = "pineapple"
for fruit in fruits:
    print(fruit)

fruits.append("jackfruit")#add element at end of list
fruits.remove("jackfruit")

fruits.insert(0, "blueberry")
print(fruits)
fruits.sort() #ascending order

fruits.reverse() #just reversere original order
#fruits.clear() #remove all elements
print(fruits.index("blueberry"))
print(fruits)

print(fruits.count("Banana")) #how many ties in list



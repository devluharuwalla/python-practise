#set uses curly, unorder and immutable( not change), but add remove ok, no duplicate

fruits = {"apple", "banana", "coconut", "orange"}
print(fruits)

#help(fruits) for all methods

len(fruits)

print("apple" in fruits)


#no indexing

fruits.add("pineapple")

fruits.remove("apple")

#fruits.pop() # removes first elemnt, is random
#fruits.clear()

#all duplicates are removed, only one copy stays

print(fruits)
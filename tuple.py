#surrounded by parenthisis
#ordered unchangebale, duplicates ok, but faster than list


# uses ()

fruits = ("apple", "orange", "banana", "coconut", "coconut")

#dir(fruits)
#help(fruits)

len(fruits)

print("pineapple" in fruits)

print(fruits.index("apple")) #gives index possiiton
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)

print(fruits)

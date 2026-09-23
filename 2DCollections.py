fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chciken", "fish", "turkey"]
#witing seperate lists inside groceries seperate with commas works too
groceries = [fruits, vegetables, meats]

print(groceries)

print(groceries[0]) #fruits list, index 1 is meats, index 2 is meats

print(groceries[0][0]) #apple from groceries, so row 0, column 0



for collection in groceries:
    for food in collection:
        print(food, end = ' ')
    print() #iterates all elements

    #can do for tuple and sets
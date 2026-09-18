for x in range(1, 10):
    print(x, end="") #for same line, because defsult for loop is new line


rows = int(input("enter number of rows: "))
columns = int(input("enter number of columns: "))

symbol = input("enter symbol to use: ")


for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print() #prrints new line



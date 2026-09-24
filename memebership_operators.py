




word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word: #return true or false
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")



if letter not in word: #return true or false opposite of in
    print(f"{letter} was not found")
else:
    print(f"there is {letter}")

students = {"spongebob", "Patrick", "Sandy"}

student = input("Enter name")

if student in students:
    print(f"{student} is a student")

else:
    print(f"{student} was not found")


grades = {"Sandy" : "A", "Squidward" : "B", "Spongebob" : "C" , "Patrick" : "D"}

student = input("enter name: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not found")



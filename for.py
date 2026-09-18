
 #second num exclusive
for x in range(1, 11):
    print(x)

for x in reversed(range(1, 11)):
    print(x)

print("Happy new year!")

for x in range(1, 11, 2):
    print(x)


credit_card = "1234-5959-3222-4455"

for x in credit_card:
    print(x)
#skips 13
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
#leave at 13
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)


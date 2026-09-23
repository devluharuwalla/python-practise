

def happy_birthday(name, age):
    print(f"happy bday {name}")
    print(f"you are {age} old")
    print(f"happy bday {name}")
    print()


happy_birthday("Bro", 35)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"your bill of ${amount: .2f} is due oon {due_date}")


display_invoice("DEV", 42.50, "01/05")

def add(x, y):
    z =x+y
    return z
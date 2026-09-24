

def add(*args): #you need * most important
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1,2,3,4,5))

def display_name(*args):
    for arg in args:
        print(arg, end= " ")
    


print(display_name("Dr", "googa"))

def print_adress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_adress(street="123 fake st", city="Detroit", state="MI", zipcode="54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("Dr. ", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               statee="MI",
               zip="54321")
               
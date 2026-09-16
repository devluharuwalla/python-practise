import math

print("hello")

first_name = "bro"
print("hello " + first_name)

print(f"Hello {first_name}") 

is_student = True

if is_student:
    print("you r student")
else:
    print("you are not student")


name = "brocode"
age = 25
gpa = 3.2
is_student = True

print(type(name))

gpa = int(gpa)

print(gpa)

print(float(age))

#name = input("whats ur name")

print(f"your name is {name}")


friends = 10
friends += 1
friends -= 2
friends*=3
print(friends)

friends = friends ** 2 #to the power of
friends **= 2

remainder = friends % 3
x = 3.4
result = round(x)

y = -4

result = abs(y)
print(result)

z = 5
result = pow(4,3)
print(result)

result = max(8, 25, -3)
result = min(3, 50, -4)

print(result)


#have to import math for pi, e and stuff

print(math.pi)
x = 9.2
#result = math.sqrt(9)
#result = math.ceil(x)
result = math.floor(x)
print(result)
radius = float(input("enter radius of circle"))

circumference = 2*math.pi*radius
print(f"the circumference is {round(circumference, 2)}")

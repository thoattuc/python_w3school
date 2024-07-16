# variable = value
x = 5
y = "Niam"

print(x)
print(y)

# var name
myvar = "niam"
my_var = "niam"
myVar = "niam"
MYVAR = "niam"
myvar01 = "niam"
_my_var = "niam"

# many value to multiple variable
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value to multiple variable
x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# output variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

# global variable
x = "awesome"


def myfunc1():
    print("Python is " + x)


myfunc1()
# global keyword


def myfunc2():
    global x
    x = "fantastic"


myfunc2()

print("Python is " + x)

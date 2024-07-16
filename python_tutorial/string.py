# string:
a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# string are arrays:
a = "Hello, World!"
print(a[0])

# looping through a string:
for item in "banana":
    print(item)

# check string:
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

# slicing string:
b = "Hello, World!"
print(b[2:5])
print(b[2:])
print(b[:5])
print(b[-5:-2])

# modify string
a = "Hello, Niam"
print(a.upper())    # HELLO, NIAM
print(a.lower())    # hello, niam
print(a.swapcase())     # hELLO, nIAM
print(a.capitalize())   # Hello, Niam
print(a.title())        # Hello, Niam

a = " Hello, Niam"
print(a.strip())    # remove whitespace

a = "Hello, Niam"
print(a.replace("H", "J"))

print(a.split(","))    # ['Hello', ' Niam'] (returns a list where the text between the specified separator)

# string concatenation:
a = "Hello"
b = "World"
c = a + b
print(c)    # HelloWorld

c = a + " " + b
print(c)    # Hello World

# format string:

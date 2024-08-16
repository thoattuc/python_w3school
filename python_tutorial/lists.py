"""
    Lists are used to store multiple items in a single variable.
    List items are ordered, changeable, and allow duplicate values.
    Lists are created using square brackets [].
"""

mylist = ["apple", "banana", "cherry"]
print(mylist)

this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(this_list)


# The list() Constructor
this_list = list(("apple", "banana", "cherry"))
print(this_list)

# Access Items:
this_list = ["apple", "banana", "cherry"]
print(this_list[1])
print(this_list[-1])    # cherry

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])
print(this_list[:4])
print(this_list[2:])
print(this_list[-4:-1])

if "apple" in this_list:
    print("Yes, 'apple' is in the fruits list")

# Loop lists
this_list = ["apple", "banana", "cherry"]
for x in this_list:
    print(x)

for i in range(len(this_list)):
    print(this_list[i])

i = 0
while i < len(this_list):
    print(this_list[i])
    i = i + 1

# Shorthand for loop:
[print(x) for x in this_list]

# List comprehension:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)

print(new_list)

# new_list = [_expression for _item in _iterable if _condition == True]
new_list = [x for x in fruits if x != "apple"]
print(new_list)

# Sort lists:
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort()
print(this_list)

list_numbers = [100, 50, 65, 82, 23]
list_numbers.sort(reverse=True)
print(list_numbers)

# Copy lists:
this_list = ["apple", "banana", "cherry"]
my_list = this_list.copy()
print(my_list)

my_list = list(this_list)
print(my_list)

my_list = this_list[:]
print(my_list)

# Join lists:
list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]

list_3 = list_1 + list_2
print(list_3)

# for x in list_2:
#     list_1.append(x)
# print(list_1)

list_1.extend(list_2)
print(list_1)

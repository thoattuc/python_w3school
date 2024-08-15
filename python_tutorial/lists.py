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

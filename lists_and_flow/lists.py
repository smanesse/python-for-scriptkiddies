list_of_strings = ["hello", "world", "is", "the", "first", "program", "always"]
# print each element on a new line
for s in list_of_strings:
    print(s)

# join together using the first string as a separator:
joined = " ".join(list_of_strings)
print(joined)

# first element
first = list_of_strings[0]

# last element
last = list_of_strings[-1]

# first 3 elements
first_three = list_of_strings[:3]

# everything but the first three elements
all_but_first_three = list_of_strings[3:]

# adding lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
added_lists = l1 + l2
print(added_lists)

# adding an element to an existing list
# notice this edits the original list instead of returning a new list with the added element
lsit_of_strings.append("!!!!")
print(list_of_strings)


list_of_ints = [1, 2, 3, 4, 5, 6]


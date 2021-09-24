s1 = "first string"
s2 = "second string"

# put strings together
appended = s1 + s2
print(appended)

# split on space
list_of_words = s1.split(" ")
print(list_of_words)

# first letter
first_letter = s1[0]
print(first_letter)

# third letter
third_letter = s1[2]
print(third_letter)

# first 5 letters
first_five = s1[:5]
print(first_five)

# everything but the first 4 letters:
all_but_last_four = s1[4:]
print(all_but_last_four)

# last letter:
last_letter = s1[-1]
print(last_letter)

# starting and ending whitespace removed
whitespace_word = "   \n  \t lots of spaces    there aren't    there     \n \t"
stripped = whitespace_word.strip()
print(stripped)

# upper case
upper = s1.upper()
print(upper)

# check if string is in string
result = "first" in s1
print(result)








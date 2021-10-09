# writing files
# "w" is for write
with open("out.txt", "w") as f:
    f.write("this is my file!")

# reading files
# "r" is for read
with open("out.txt", "r") as f:
    print(f.read())

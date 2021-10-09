# create a dictionary
d = {"my_key": "my_value"}

# get something from the dictionary
val = d["my_key"]
val = d.get("my_key")
# this will return an empty string if the key is not in the dictionary
val = d.get("bogus", "")

for key, value in d.items():
    print(key, value)


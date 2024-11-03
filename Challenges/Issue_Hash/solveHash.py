import json

# target hash
target_hash = "ec44b366a89bb2ba78d6b8e5e81194d596d301b7"

# load rainbow table
with open("rainbow_table.json", "r") as f:
    rainbow_table = json.load(f)

# check if target hash is in rainbow table
plaintext = rainbow_table.get(target_hash)

if plaintext:
    print(f"{plaintext}")
else:
    print("Hash not found in rainbow table")

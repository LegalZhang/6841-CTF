import hashlib
import gzip
import json

rainbow_table = {}

# create rainbow table
with gzip.open('crackstation.txt.gz', 'rt', encoding='ISO-8859-1') as f:
    for line in f:
        password = line.strip()
        sha1_hash = hashlib.sha1(password.encode()).hexdigest()
        rainbow_table[sha1_hash] = password

# save rainbow table to json file
with open("rainbow_table.json", "w") as f:
    json.dump(rainbow_table, f)

print("Rainbow table has been created 'sha1_rainbow_table.json'")

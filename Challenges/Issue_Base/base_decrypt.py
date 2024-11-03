import base64

with open("base.txt", "r") as f:
    data = f.read().strip()

flag16 = base64.b16decode(data)

flag32 = base64.b32decode(flag16)

flag64 = base64.b64decode(flag32).decode("utf-8")

print(flag64)
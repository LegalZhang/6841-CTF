import base64

with open("flag.txt") as f:
    flag = f.read().strip()

# base64 encode the flag
flag64 = base64.b64encode(flag.encode())

# base32 encode the flag
flag32 = base64.b32encode(flag64)

# base16 encode the flag
flag16 = base64.b16encode(flag32)

with open("base.txt", "w") as f:
    f.write(flag16.decode())
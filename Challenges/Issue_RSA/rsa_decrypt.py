import base64
import libnum
from math import isqrt

def fermat(n):
    a = isqrt(n) + 1
    while True:
        b2 = a * a - n
        b = isqrt(b2)
        if b * b == b2:
            return a + b, a - b
        a += 1

with open("public_key.txt", "r") as f:
    lines = f.readlines()
    n = int(lines[0].split("=")[1].strip())
    e = int(lines[1].split("=")[1].strip())

with open("ciphertext.txt", "r") as f:
    ciphertext_base64 = f.read().strip()

ciphertext_bytes = base64.b64decode(ciphertext_base64)
c = libnum.s2n(ciphertext_bytes)

p, q = fermat(n)

phi_n = (p - 1) * (q - 1)
d = libnum.invmod(e, phi_n)

m = pow(c, d, n)

flag = libnum.n2s(m)
print(flag)

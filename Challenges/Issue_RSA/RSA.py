import base64
import libnum
import gmpy2
from Crypto.PublicKey import RSA

p=libnum.generate_prime(1024)
q=int(gmpy2.next_prime(p))
e=65537
m="flag{guess}"
m=libnum.s2n(m)
n=p*q
c=pow(m,e,n)

with open("public_key.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")

flag_c = libnum.n2s(c)
flag_base64 = base64.b64encode(flag_c).decode("utf-8")
with open("ciphertext.txt", "w") as f:
    f.write(flag_base64)
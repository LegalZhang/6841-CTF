from Crypto.Util.number import inverse

# known RSA values
p = 6841
q = 6959
e = 65537

# calculate n
n = p * q

# calculate phi(n)
phi_n = (p - 1) * (q - 1)

# calculate d
d = inverse(e, phi_n)

# print flag
print(f"flag{{n={n},d={d}}}")

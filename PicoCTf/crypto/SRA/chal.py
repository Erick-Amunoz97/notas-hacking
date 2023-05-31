from Crypto.Util.number import getPrime, inverse, bytes_to_long
from string import ascii_letters, digits
from random import choice

plain = "".join(choice(ascii_letters + digits) for _ in range(16))
p = getPrime(128) #gluttony
q = getPrime(128) #greed

n = p * q # lust
e = 65537 # sloth
phi = (p - 1) * (q - 1)  #envy
d = inverse(e, phi) #envy
cipher = pow(bytes_to_long(plain.encode()), e, n)



print(f"{n = }")
print(f"{cipher = }")
print(f"{d = }")

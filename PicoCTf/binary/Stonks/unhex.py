from binascii import unhexlify
flag = b"".join(
	[ 
	unhexlify("6f636970")[::-1], 
	unhexlify("7b465443")[::-1],
	unhexlify("306c5f49")[::-1], 
	unhexlify("345f7435")[::-1],
	unhexlify("6d5f6c6c")[::-1],
	unhexlify("306d5f79")[::-1], 
	unhexlify("5f79336e")[::-1], 
	unhexlify("38343136")[::-1], 
	unhexlify("34356562")[::-1], 
	unhexlify("007d")[::-1], 
	]
).decode() 

print(flag)
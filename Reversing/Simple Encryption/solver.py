#! /bin/python3
# Follow me on Ironbyte.me

# ##################
# Author => IronByte
# ##################

enc_flag = b'\x70\x05\xbf\xde\x51\x09\xb2\xce\x57\x13\xa7\x9e\x12\x0d\xac\x9a\x10\x3f\xe8\x9e\x7c\x54\xed\xdc\x17\x19\xe9\xc5\x10\x18\xeb\xd6'
key = b'\x23\x60\xdc\xab'

flag = ""
for i in range(len(enc_flag)):
    print(chr(enc_flag[i] ^ key[i % len(key)]), end="")
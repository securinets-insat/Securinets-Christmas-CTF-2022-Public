#! /bin/python3

# ##################
# Author => IronByte
# ##################

key = b"\x23\x60\xdc\xab"
flag = b'Securinets{51mp13_45_41w4y5n3x7}'
enc_flag = b''

for i in range(len(flag)):
    enc_flag += bytes([flag[i] ^ key[i % len(key)]])
print(''.join(r'\x'+hex(letter)[2:] for letter in enc_flag))
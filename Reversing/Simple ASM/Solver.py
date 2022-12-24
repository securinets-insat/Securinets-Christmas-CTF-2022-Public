#! /bin/python3
# Follow me on ironbyte.me

# ##################
# Author => IronByte
# ##################

# O(N) Solution.
def reverseBits(n):
    rev = 0
    while (n > 0):
        rev = rev << 1
        if (n & 1 == 1):
            rev = rev ^ 1
        n = n >> 1
    return hex(rev)

# O(1) Solution.
def reverseBits_Optimized(x):
    x = (x & 0x55555555) << 1 | (x & 0xAAAAAAAA) >> 1
    x = (x & 0x33333333) << 2 | (x & 0xCCCCCCCC) >> 2
    x = (x & 0x0F0F0F0F) << 4 | (x & 0xF0F0F0F0) >> 4
    x = (x & 0x00FF00FF) << 8 | (x & 0xFF00FF00) >> 8
    x = (x & 0x0000FFFF) << 16 | (x & 0xFFFF0000) >> 16
    return hex(x)


value = 0xc848b3d5
print("Value with the unOpt : ", reverseBits(value));
print("Value with the Opt : ", reverseBits_Optimized(value))

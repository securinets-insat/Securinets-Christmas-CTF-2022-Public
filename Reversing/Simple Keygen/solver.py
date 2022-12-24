#! /bin/python3
# Follow me on Ironbyte.me

# ##################
# Author => IronByte
# ##################
 
# Username = Ironbyte1234

def solve(password):
    ascii = [ord(elt) for elt in password]
    flag = []
    for i in range(len(ascii)): 
        flag.append((ascii[i] - i) ^ 0x01)
    print("Username = ", "".join([chr(elt) for elt in flag])) 
    
solve("Htprg}{k8<<@")
#! /bin/python3
# Follow me on Ironbyte.me

# ##################
# Author => IronByte
# ##################

inp = "Ucestohcru}l2p2Y>4s15Y`64e7h?Y73Y36Ye667'{"
ascii = [ord(elt) for elt in inp]

def breaker():
    for guess1 in range(0xff):
        for guess2 in range(0xff):
            flagGuess = ""
            for elt in ascii:
                flagGuess = flagGuess + chr(elt ^ guess1 ^ guess2)
            if ("Securinets{" in flagGuess):
                print("Flag = ", flagGuess)
                print("The 1st byte = ", guess1)
                print("The 2nd byte = ", guess2)
                return
breaker()
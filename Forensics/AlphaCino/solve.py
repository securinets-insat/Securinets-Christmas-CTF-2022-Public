from PIL import Image

def bin2file(bin):
        data = bytearray()
        for b in range(len(bin)//8):
             data.append(int(bin[b*8:(b+1)*8],2))
        return bytes(data)

def solve():
    image=Image.open("Alphacino.png")
    pixels=list(image.getdata())
    data=""
    for i in range (len(pixels)):
        pixel=list(pixels[i])
        data+=str(255-pixel[3])
    file=open("image.png","wb")
    file.write(bin2file(data))
    file.close()
    

solve()

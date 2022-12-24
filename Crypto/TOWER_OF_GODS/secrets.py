from Crypto.Util.number import getPrime,long_to_bytes,bytes_to_long,isPrime,inverse
import json
from random import randint,shuffle


class Outer_tower():
    def __init__(self,flag):
        self.flag=bytes_to_long(flag)
        self.p=getPrime(1024)
        self.e=65537
    def encrypt_flag(self):
        return json.dumps({"encrypted_flag":pow(self.flag,self.e,self.p)})
    def encrypt(self,msg):
        return json.dumps({"encrypted_msg":pow(int(msg,16),self.e,self.p)})
    def start_floor_test(self):
        while True:
            your_input=json.loads(input())
            if not 'option' in your_input:
                    return {"error": "U better choose something or die alone"}
            elif your_input['option'] == 'get_flag':
                print(self.encrypt_flag())

            elif your_input['option'] == 'sign':
                try :
                    msg = your_input['msg']
                    print(self.encrypt(msg))
                except:
                    pass
            elif your_input['option']=='return to tower':
                break
            else:
                return {"error": "Invalid option"}



class Flour_of_test():
    def __init__(self,flag):
        self.flag=bytes_to_long(flag)
        self.e=3
    def encrypt_flag(self):
        p=getPrime(512)
        q=getPrime(512)
        n=p*q
        return json.dumps({"encrypted_flag":pow(self.flag,self.e,n),"N":n,"e":3})
    def encrypt(self,msg):
        p=getPrime(512)
        q=getPrime(512)
        n=p*q
        return json.dumps({"encrypted_msg":pow(int(msg,16),self.e,n),"N":n})
    def start_floor_test(self):
        while True:
            your_input=json.loads(input())
            if not 'option' in your_input:
                    return {"error": "U better choose something or die alone"}
            elif your_input['option'] == 'get_flag':
                print(self.encrypt_flag())

            elif your_input['option'] == 'sign':
                try :
                    msg = your_input['msg']
                    print(self.encrypt(msg))
                except:
                    pass
            elif your_input['option']=='return to tower':
                break
            else:
                return {"error": "Invalid option"}








class The_Workshop_Battle():
    def __init__(self,flag):
        self.flag=bytes_to_long(flag)
        self.q=getPrime(512)
        self.p=getPrime(512)
        self.phi=(self.p-1)*(self.q-1)

        self.n=self.p*self.q
        self.e=65537
        self.d=inverse(self.e,self.phi)
    def sign(self,msg):
        if b"admin" not in bytes.fromhex(msg):
            return json.dumps({"signature":hex(pow(int(msg,16),self.d,self.n)),"N":self.n,"e":self.e})
        else:
            return json.dumps({"signature":pow(31066278741462331364812614761,self.d,self.n),"N":self.n,"e":self.e})
    def verify(self,signature):
        signature=pow(int(signature,16),self.e,self.n)
        if long_to_bytes(signature)==b"admin":
            return long_to_bytes(self.flag)
        else:
            return "get out Regular !"
    def start_floor_test(self):
        while True:
            your_input=json.loads(input())
            if not 'option' in your_input:
                    return {"error": "U better choose something or die alone"}
            elif your_input['option'] == 'sign':
                msg = your_input['msg']
                print(self.sign(msg))

            elif your_input['option']=="verify":

                sig=your_input["signature"]
                print(self.verify(sig))

            elif your_input['option']=='return to tower':
                break
            else:
                return {"error": "Invalid option"}





class Hell_train():
    def __init__(self,flag):
        self.flag=bytes_to_long(flag)
        self.q=getPrime(512)
        self.p=self.getsmoothprime(512)
        self.n=self.p*self.q
        self.e=65537
        self.check=0
    def getsmoothprime(self,size):
        f=eval(open('primes.txt','r').read())
        shuffle(f)
        p=2
        i=0
        while True:
            p=p*f[i]
            if isPrime(p+1) and len(bin(p))>size:
                return p+1
            i+=1
            if len(bin(p))>2*size:
                shuffle(f)
                i=0
                p=2
    def encrypt_flag(self):
        if self.check==0:
            self.check=1
            return json.dumps({"encrypted_flag":pow(self.flag,self.e,self.n),"N":self.n,"e":self.e})
    def encrypt(self,msg):
        return json.dumps({"encrypted_msg":pow(int(msg,16),self.e,self.n),"N":self.n,"e":self.e})
    
    def start_floor_test(self):
        while True:
            your_input=json.loads(input())
            if not 'option' in your_input:
                    return {"error": "U better choose something or die alone"}
            elif your_input['option'] == 'get_flag':
                print(self.encrypt_flag())

            elif your_input['option'] == 'encrypt':
                try :
                    msg = your_input['msg']
                    print(self.encrypt(msg))
                except:
                    pass
            elif your_input['option']=='return to tower':
                break
            else:
                return {"error": "Invalid option"}



class FLOOR_OF_DEATH():
    def __init__(self,flag):
        self.flag=bytes_to_long(flag)
        self.q=getPrime(512)
        self.p=(self.getsmoothprime(512)-1)
        self.n=self.p*self.q
        self.e=109480
    def getsmoothprime(self,size):
        f=eval(open('primes.txt','r').read())
        shuffle(f)
        p=2*23**2
        i=0
        while True:
            p=p*f[i]
            if isPrime(p+1) and len(bin(p))>size:
                return p+1
            i+=1
            if len(bin(p))>2*size:
                i=0
                shuffle(f)
                p=2

    def encrypt_flag(self):
        return json.dumps({"encrypted_flag":pow(self.flag,self.e,self.n),"N":self.n,"e":self.e})
    def encrypt(self,msg):
        return json.dumps({"encrypted_msg":pow(int(msg,16),self.e,self.n),"N":self.n,"e":self.e})
    
    def start_floor_test(self):
        while True:
            your_input=json.loads(input())
            if not 'option' in your_input:
                    return {"error": "U better choose something or die alone"}
            elif your_input['option'] == 'get_flag':
                print(self.encrypt_flag())

            elif your_input['option'] == 'encrypt':
                try :
                    msg = your_input['msg']
                    print(self.encrypt(msg))
                except:
                    pass
            elif your_input['option']=='return to tower':
                break
            else:
                return {"error": "Invalid option"}


## For Mirror World i just didnt want to make the challenge hard so i removed the padding 
## (its the same task as the second one but it tricks some people into overthinking)
            
class Mirror_World():
    def __init__(self,flag):
        self.flag=bytes_to_long(flag)
        self.q=getPrime(512)
        self.p=getPrime(512)
        self.n=self.p*self.q
        self.e=3
        self.check=0
        
    def encrypt_flag(self):
        if self.check!=1:
            self.check+=1
            x=randint(0,self.n-1)
            y=randint(0,self.n-1)
            padded_flag=(x*self.flag+y)%self.n
            return json.dumps({"encrypted_flag":pow(self.flag,self.e,self.n),"N":self.n,"e":self.e,"X":x,"Y":y})
        else:
            return json.dumps({"ALERT":"You cant fool zahard 2 times regular"})
    def encrypt(self,msg):

        return json.dumps({"encrypted_msg":pow(int(msg,16),self.e,self.n),"N":self.n,"e":self.e})
    
    def start_floor_test(self):
        while True:
            your_input=json.loads(input())
            if not 'option' in your_input:
                    return {"error": "U better choose something or die alone"}
            elif your_input['option'] == 'get_flag':
                print(self.encrypt_flag())

            elif your_input['option'] == 'sign':
                try :
                    msg = your_input['msg']
                    print(self.encrypt(msg))
                except:
                    pass
            elif your_input['option']=='return to tower':
                break
            else:
                return {"error": "Invalid option"}




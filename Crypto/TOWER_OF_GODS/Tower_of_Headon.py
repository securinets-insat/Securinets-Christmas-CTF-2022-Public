from secrets import Outer_tower,Flour_of_test,The_Workshop_Battle,Hell_train,FLOOR_OF_DEATH,Mirror_World
import json
flag_1=open("flag_1.txt",'rb').read()
flag_2=open("flag_2.txt",'rb').read()
flag_3=open("flag_3.txt",'rb').read()
flag_4=open("flag_4.txt",'rb').read()
flag_5=open("flag_5.txt",'rb').read()
flag_6=open("flag_6.txt",'rb').read()






class Headon():
    def __init__(self):
        self.before_input = "Welcome to Tower of GOD"
        self.floor_cleared=0
        self.flags=[flag_1,flag_2,flag_3,flag_4,flag_5,flag_6]
    def The_Path_of_God(self,your_input):

        if your_input>self.floor_cleared and your_input>6:
            print("You can't skip floor know your place well regular")
        else:
            match abs(your_input):
                case 0:
                    print(open("Outer_tower.txt",'r').read())
                    The_irregular_test=Outer_tower(flag_1)
                    The_irregular_test.start_floor_test()
                case 1:
                    print(open("Flour_of_test.txt",'r').read())
                    Rak_the_ragnarok=Flour_of_test(flag_2)
                    Rak_the_ragnarok.start_floor_test()
                case 2:
                    print(open("The_Workshop_Battle.txt",'r').read())
                    Fugitive=The_Workshop_Battle(flag_3)
                    Fugitive.start_floor_test()
                case 3:
                    print(open("Hell_train.txt",'r').read())
                    Zahard=Hell_train(flag_4)
                    Zahard.start_floor_test()
                case 4:
                    print(open("FLOOR_OF_DEATH.txt",'r').read())
                    Khun=FLOOR_OF_DEATH(flag_5)
                    Khun.start_floor_test()
                case 5:
                    print(open('Mirror_World.txt','r').read())
                    Arlen_Grace=Mirror_World(flag_6)

                    Arlen_Grace.start_floor_test()

                
    def submit_test(self,flag):
        if flag in self.flags:
            self.floor_cleared=self.flags.index(flag)+1
        else:
            print("stupid regular")
    def controle_fate(self):
     while True:
        try:
            your_input=json.loads(input())
            if (not 'option' in your_input) or (not "input" in your_input ):
                    return {"error": "U better choose something or die alone"}
            elif your_input['option'] == 'The_Path_of_God':
                choice=abs(your_input["input"])
                self.The_Path_of_God(choice)

            elif your_input['option'] == 'test':
                flag=your_input["input"].encode()
                self.submit_test(flag)
                print(f"You are on Floor {self.floor_cleared}")
            else:
                return {"error": "Invalid option"}
        except Exception as e:
            print(json.dumps({"Zahard":"I killed you before and I will kill you again"}))

TOWER_OF_GOD=Headon()
TOWER_OF_GOD.controle_fate()


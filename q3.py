class Card: 
    def __init__(self,num,color):

        self.__num = num 
        self.__color = color 


global numbers_chosen
numbers_chosen = []*29


def ChooseCard(): 
    global numbers_chosen
    flag = True 
    while flag == True: 
        card_selected = int(input("Enter a number from 1 and 30: "))
        if card_selected < 1 and card_selected > 30: 
            print("Enter a valid number")
        elif numbers_chosen[card_selected-1] == True: 
            print("Already taken") 
        else: 
            print("Valid")
            flag = False 
    numbers_chosen[card_selected - 1] = True 
    return card_selected - 1  


def Getnum(self):
    return self.__num 

def Getcolor(self): 
    return self.__color


Array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
try: 
    Filename = "CardValues.txt"
    File = open(Filename,'r')
    for i in range (0,30): 
        NumberRead = int(File.readline()) 
        ColorRead = File.readline() 
        Array[i] = Card(NumberRead,ColorRead)
    File.close 
except IOError: 
    print("Could not open file")

print(Array)

player1 = [] 
for x in range(0,4): 
    return_number = ChooseCard() 
    player1.append(Array[return_number])
for x in range(0,4): 
    print(player1[x].Getcolor())
    print(player1[x].Getnum()) 





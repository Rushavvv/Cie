'''Q1'''

# TheData = [20,3,4,8,12,99,4,26,4] 

# def insertion_sort(TheData): 
#     for count in range(0,len(TheData)): 
#         data_to_insert = TheData[count]
#         inserted = 0 
#         Nextval = count - 1
#         while Nextval >= 0 and inserted != 1: 
#             if data_to_insert < TheData[Nextval]: 
#                 TheData[Nextval + 1] = TheData[Nextval]
#                 Nextval = Nextval - 1
#                 TheData[Nextval + 1] = data_to_insert
        
#             else: 
#                 inserted = 1
#     return data_to_insert
            
            
# def output(TheData): 
#     for i in range(0,len(TheData)): 
#         print(TheData[i]) 
    
# print("Before")
# print(output(TheData))

# print("after") 
# insertion_sort(TheData)
# print(TheData)


# def check(TheData): 
#     val = int(input("Enter a number to check"))
#     for i in range(0, len(TheData)): 
#         if TheData[i] == val: 
#             print("Found")
#             return True
         
#     print("Not found")
#     return False 

# print(check(TheData))


''' Q2'''

class HiddenBox: 
    # __BoxName String
    # __Creator String
    # __DateHidden String
    # __GameLocation String
    # __LastFinds [10][2] String
    # __Active String

    def __init__(self,boxname,creator,date,location): 
        self.__boxname = boxname 
        self.__creator = creator 
        self.__date = date 
        self.__location = location
        self.__finds = [["" for i in range(0,2) for j in range(0,10)]] 
        self.__active = False  
        


        def GetBoxName(): 
            return self.__boxname 

        def GetGameLocation(): 
            return self.__location

TheBoxes = [HiddenBox("","","","") for i in range(0,10000)]






def newbox(TheBox,NumBox):
    boxname = input("Enter box name") 
    creator = input("Enter creator")
    date = input("Enter date hidden")
    location = input("enter location hidden")
    TheBox[NumBox] = HiddenBox(boxname,creator,date,location)
    return(NumBox+1)
    

class puzzlebox(HiddenBox): 
    # __PuzzleText String # __Solution String def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation, NewPuzzleText, NewSolution): 
    # super().__init__(NewBoxName, NewCreator, NewDateHidden, NewLocation)
    # self.__PuzzleText = NewPuzzleText 
    # self.__Solution = NewSolution
    

    



  
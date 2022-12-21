# Player 01 vs Player 02
import functions

def gameMode01 ():
    
    print("Make sur Player 02 does not see your number")
    p1Num = int(input("Give your number (Bteween 0 and 100) : "))
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


    I = functions.rangeCheck(0,100, p1Num)
    tryNum = 10  #Number of try
    
    while I :
        while i < tryNum: 
            p2Num = int(input("Give your number here: "))
            
            if p1Num == p2Num:
                i = True
            else:
                i+=1
    
    if I == False:
        print("Make sur your number is between 0 and 100")

    if p1Num == True:
        print("\n\n\t Player 02 Wins")
    else:
        print("\n\n\t Player 01 Wins")

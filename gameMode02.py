# Player 01 vs AI

import functions



def gameMode02 ():
    # Player choosing 

    print("Give us a number and the Ai is gonna try to find it")
    p1Num = int(input("Give your number: "))
    
    I = functions.rangeCheck(0, 100, p1Num)
    
    if I == False :
        print ("Make sur your number is between 0 and 100")
    
    while I :
        functions.search(p1Num)
        I = False
    
    if I == False :
        print ("Make sur your number is between 0 and 100")

gameMode02()
print (" You loose")
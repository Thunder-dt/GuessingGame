def winning(i):
    if i == 10 :
        print(" \n\n\n Game Over.\n Player 01 wins ")
    else:
        print("Player 02 wins")

def numCheck (minX, maxX, x):
    if x < minX or x > maxX :
        print("Make sur youur number is between "+minX+" and "+maxX)
        x = False
    else :
        x = True
    return x
 
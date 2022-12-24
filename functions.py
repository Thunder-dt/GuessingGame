# Functing to check if the number is in range
def rangeCheck( minx , maxx , x ):
    if x > maxx or x < minx :
        y = False  # y for not changing the value of the number
    else :
        y = True
    return y

# Ai Algo

def search(p1Num):
    max = 100
    min = 0
    s = 0

    while s != p1Num:
        s = (max + min)//2
        print(s)
        if s > p1Num :
            max = s
        else :
            min = s
        
        if s == p1Num:
            return False 

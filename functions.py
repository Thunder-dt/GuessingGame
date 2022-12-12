# Functing to check if the number is in range
def rangeCheck( minx , maxx , x ):
    if x > maxx or x < minx :
        y = False  # y for not changing the value of the number
    else :
        y = True
    return y


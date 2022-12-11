print("--------------------------Game--------------------------")

# P1 VS P2
print("Enter a number and make sure that P2 Doesnt see it.")
p1Num = input("Make sur it's between 0 and 100 : ")

p1Num = int(p1Num)

i = 0
"""
if p1Num >= 0 and p1Num <= 100:    # Checking if p1Num is valide


    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Guess Player1 number")
    

    while i < 10:
        p2Num = input("Enter the number ")
        p2Num = int(p2Num)

        if p2Num == p1Num:
            break
        elif p2Num > p1Num:
            print("Too big")
        else:
            print("Too small") 
        i+=1

"""


# P1 Vs Ai
# P1 guessing 
p2Num = range(0,101)
num = []
for j in p2Num:
    num.append(j)
print(num[50])


# AI guessing



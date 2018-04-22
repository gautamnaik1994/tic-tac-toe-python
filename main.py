r,c=3,3
mainArray = [[0 for x in range(r)] for y in range(c)]

def printGrid():
    for i in range(len(mainArray)):
        for j in range(len(mainArray[i])):
            if(mainArray[i][j]== 0):
                print("|" + str(i) + str(j)+ "|" ,end="")
            else:
               print("|" + str(mainArray[i][j]) + " |" ,end="")
        print("",end="\n")

printGrid()

def getUserInput():
    return input("Enter position: ")


def checkWinCondition(val,userSign):
    value=str(val)
    x=int(value[0])
    y=int(value[1])
    mainArray[x][y]=userSign
    printGrid()

    for i in range(r):
        if(mainArray[x][i]!=userSign):
            break
        if(i==r-1):
            print("Winner"+ userSign)

    for i in range(r):
        if(mainArray[i][y]!=userSign):
            break
        if(i==r-1):
             print("Winner"+ userSign)

    for i in range(r):
        if(mainArray[i][i]!=userSign):
            break
        if(i==r-1):
             print("Winner"+ userSign)

    if(x+y==(r-1)):
        for i in range(r):
            if(mainArray[i][(r-1)-i] != userSign):
                break;
            if(i == r-1):
                print("Winner"+ userSign)

turnCount = 0;
while turnCount < 9:
    firstUserInput = getUserInput()
    checkWinCondition(firstUserInput,'X')
    secondUserInput = getUserInput()
    checkWinCondition(secondUserInput,'O')


Board = []
Col1 = []
Col2 = []
Col3 = []
Col4 = []
Col5 = []
Col6 = []    #Working on CheckAdj
Col7 = []

def Col(Num) :
    if Num == 1 :
        return Col1
    elif Num == 2 :
        return Col2
    elif Num == 3 :
        return Col3
    elif Num == 4 :
        return Col4
    elif Num == 5 :
        return Col5
    elif Num == 6 :
        return Col6
    elif Num == 7 :
        return Col7

def GenBoard() :
    for i in range(1,8) :
        GenBlankCol(Col(i))

def GenBlankCol(Col) :
    for i in range(7) :
        Col.append('*')
    #print(Col)
    Board.append(Col)

def Piece(FP) :
    if FP :
        return 'X'
    else :
        return 'O'

def NotFullCol(Col) :
    if '*' in Col :
        return True
    else :
        print('full')
        return False

def PlayPiece(Col, FP) :
    if NotFullCol(Col) :
        Col[Col.index('*')] = Piece(FP) #Sets first value of blank to correct piece
        #print('placed')

def CheckHoriWin(FP) :
    #TestCol = ['O','X','X','X','X','*','*']

    WinCon = 0
    for C in range(1,8) : #Go through each collumn
        for P in Col(C) : #go through each spot -            for P in TestCol : 
            if P == Piece(FP) : #check if piece is there -   'X' : 
                WinCon += 1
                if WinCon >= 4 :
                    print(Piece(FP) + ' Won')
                    return True # Found win
            else :
                WinCon = 0
            #print(WinCon)
                
def CheckVirtWin(FP) :

    WinCon = 0
    for R in range(0,7) : #Goes through each Row
        for C in range(1,8) : #Goes through each Col
            #print(Col(C))
            if Col(C)[R] == Piece(FP) : #if piece in there
                WinCon += 1
                if WinCon >= 4 :
                    print(Piece(FP) + ' Won')
                    return True # Found win
            else :
                WinCon = 0
            #print(WinCon)
                 
def CheckDiaWin(FP, colNum) :
    '''
    #Find spot in column
    col = Col(colNum)
    if '*' in col :
        Spot = col.index('*') - 1
    else :
        Spot = 6
    #CheckAdj(Piece(FP), Spot, colNum, WinNum)
    #UpDiaCheck(Piece(FP), Spot, colNum)
    '''
    if LtoRCheck(Piece(FP)) :
        return True
    if RtoLCheck(Piece(FP)) :
        return True

def LtoRCheck(P) :
    WinNum = 0
    for C in range(1,5) : #Column
        for S in range(0,4) : #Spot
            for i in range(0,4) : #move
                if P == Col(C + i)[S + i] :
                    WinNum += 1
                    if WinNum >= 4 :
                        print(P + ' WON')
                        return True
                else :
                    WinNum = 0
    '''
    Col(1)[0-3]
    Col(2)[0-3]
    Col(3)[0-3]
    Col(4)[0-3]
    '''

def RtoLCheck(P) :
    WinNum = 0
    for C in range(1,5) : #Column
        for S in range(3,7) : #Spot
            for i in range(0,4) : #move
                if S - i >= 0 :
                    if P == Col(C + i)[S - i] :
                        WinNum += 1
                        if WinNum >= 4 :
                            print(P + ' WON')
                            return True
                    else :
                        WinNum = 0
    '''
    Col(1)[3-6]
    Col(2)[3-6]
    Col(3)[3-6]
    Col(4)[3-6]
    '''

def CheckWin(FP, colNum) :
    if CheckHoriWin(FP) :
        return True
    if CheckVirtWin(FP) :
        return True
    if CheckDiaWin(FP, colNum) :
        return True

def PrintBoard() :
    #print('PB')
    print('-----------------------------------')
    Bd = []
    for R in range(0,7) : #Goes through each Row
        E = []
        for C in range(1,8) : #Goes through each Col
            E.append(Col(C)[R])
        #print(E)
        Bd.insert(0,E)
    for C in Bd :
        print(C)

def Turn(FP) :
    num = int(input('Which col? '))
    PlayPiece(Col(num), FP)
    PrintBoard()
    return num

def Play() :
    FP = False
    GameEnd = False
    GenBoard()
    PrintBoard()
    while not GameEnd :
        if FP :
            FP = False
        else :
            FP = True
        ColNum = Turn(FP)
        if CheckWin(FP, ColNum) :
            GameEnd = True
    
Play()

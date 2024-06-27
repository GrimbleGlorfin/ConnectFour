import random, pygame, sys
from pygame.locals import *

#             NOTES
# - We want to make it so the user can play their piece by clicking on a row
# 



#Pygame Stuff
pygame.init()
clock = pygame.time.Clock()
resolution = (800, 900)
screen = pygame.display.set_mode(resolution)

board_rect = pygame.Rect(0,0,800,800)

board_pic = pygame.image.load("Connect4Board.png").convert()
board_img = pygame.transform.scale(board_pic, (800, 850))

c1_surf = pygame.Surface((50,50))


a7 = pygame.Rect(0,0, 50,50)
a6 = pygame.Rect(50,0, 50,50)
a5 = pygame.Rect(100,0, 50,50)
a4 = pygame.Rect(150,0, 50,50)
a3 = pygame.Rect(200,0, 50,50)
a2 = pygame.Rect(250,0, 50,50)
a1 = pygame.Rect(300,0, 50,50)
b7 = pygame.Rect(0,50, 50,50)
b6 = pygame.Rect(50,50, 50,50)
b5 = pygame.Rect(100,50, 50,50)
b4 = pygame.Rect(150,50, 50,50)
b3 = pygame.Rect(200,50, 50,50)
b2 = pygame.Rect(250,50, 50,50)
b1 = pygame.Rect(300,50, 50,50) 
c7 = pygame.Rect(0,100, 50,50)
c6 = pygame.Rect(50,100, 50,50)
c5 = pygame.Rect(100,100, 50,50)
c4 = pygame.Rect(150,100, 50,50)
c3 = pygame.Rect(200,100, 50,50)
c2 = pygame.Rect(250,100, 50,50)
c1 = pygame.Rect(300,100, 50,50) 
d7 = pygame.Rect(0,150, 50,50)
d6 = pygame.Rect(50,150, 50,50)
d5 = pygame.Rect(100,150, 50,50)
d4 = pygame.Rect(150,150, 50,50)
d3 = pygame.Rect(200,150, 50,50)
d2 = pygame.Rect(250,150, 50,50)
d1 = pygame.Rect(300,150, 50,50) 
e7 = pygame.Rect(0,200, 50,50)
e6 = pygame.Rect(50,200, 50,50)
e5 = pygame.Rect(100,200, 50,50)
e4 = pygame.Rect(150,200, 50,50)
e3 = pygame.Rect(200,200, 50,50)
e2 = pygame.Rect(250,200, 50,50)
e1 = pygame.Rect(300,200, 50,50) 
f7 = pygame.Rect(0,250, 50,50)
f6 = pygame.Rect(50,250, 50,50)
f5 = pygame.Rect(100,250, 50,50)
f4 = pygame.Rect(150,250, 50,50)
f3 = pygame.Rect(200,250, 50,50)
f2 = pygame.Rect(250,250, 50,50)
f1 = pygame.Rect(300,250, 50,50) 
g7 = pygame.Rect(0,300, 50,50)
g6 = pygame.Rect(50,300, 50,50)
g5 = pygame.Rect(100,300, 50,50)
g4 = pygame.Rect(150,300, 50,50)
g3 = pygame.Rect(200,300, 50,50)
g2 = pygame.Rect(250,300, 50,50)
g1 = pygame.Rect(300,300, 50,50)

Board = []
Col1 = []
Col2 = []
Col3 = []
Col4 = []
Col5 = []
Col6 = []
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
        return False

def PlayPiece(Col, FP) :
    if NotFullCol(Col) :
        Col[Col.index('*')] = Piece(FP) #Sets first value of blank to correct piece
        #print('placed')
    else :
        print('col full')
        Turn(FP)

def Turn(FP) :
    #num = int(input('Which col? '))
    num = int(random.randint(1,7))
    PlayPiece(Col(num), FP)
    PrintBoard()
    return num

def CheckHoriWin(FP) :
    #TestCol = ['O','X','X','X','X','*','*']

    WinCon = 0
    for C in range(1,8) : #Go through each collumn
        WinCon = 0
        for P in Col(C) : #go through each spot -            for P in TestCol : 
            if P == Piece(FP) : #check if piece is there -   'X' : 
                WinCon += 1
                if WinCon >= 4 :
                    print(Piece(FP) + ' Won')
                    print('Col: ' + str(C))
                    return True # Found win
            else :
                WinCon = 0
            #print(WinCon)
                
def CheckVirtWin(FP) :

    WinCon = 0
    for R in range(0,7) : #Goes through each Row
        WinCon = 0
        for C in range(1,8) : #Goes through each Col
            #print(Col(C))
            if Col(C)[R] == Piece(FP) : #if piece in there
                WinCon += 1
                if WinCon >= 4 :
                    print(Piece(FP) + ' Won')
                    print('Col: ' + str(C) + ' Row: ' + str(R))
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
            WinNum = 0
            for i in range(0,4) : #move
                #print('Col: ' + str((int(C) + int(i))) + ' Row: ' + str(int(S) + int(i) + 1))
                if P == Col(C + i)[S + i] :
                    WinNum += 1
                    #print('WinNum: ' + str(WinNum))
                    if WinNum >= 4 :
                        print(P + ' WON')
                        print('Col: ' + str(C) + ' LtR')
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
            WinNum = 0
            for i in range(0,4) : #move
                if S - i >= 0 :
                    if P == Col(C + i)[S - i] :
                        WinNum += 1
                        if WinNum >= 4 :
                            print(P + ' WON')
                            print('Col: ' + str(C) + ' RtL')
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

def InitPieces() :
    #pygame.draw.circle(a1, (0, 255, 0), [300, 300], 170, 0)
    piece = pygame.Surface((50,50))
    piece.fill((255,0,0))
    screen.blit(piece, a7.topleft)

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

def ConvertBoard() :
    for R in range(0,7) : #Goes through each Row
        for C in range(1,8) : #Goes through each Col
            width = C*100
            height = 765 - (R)*102
            if Col(C)[R] == 'X' :
                #add red
                pygame.draw.circle(screen, (255,0,0), [width,height], 47, 0)
            elif Col(C)[R] == 'O' :
                #add yellow
                pygame.draw.circle(screen, (255,255,0), [width,height], 47, 0)


Play()

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    #InitPieces()

    screen.blit(board_img,board_rect)
    #c1 = pygame.draw.circle(screen, (255,0,0), [100,251], 45, 0)
    #c1 = pygame.draw.circle(screen, (255,0,0), [100,762], 45, 0)
    #c2 = pygame.draw.circle(screen, (255,255,0), [200,250], 45, 0)
    ConvertBoard()
    pygame.display.flip()
    clock.tick(60)
    #Play()
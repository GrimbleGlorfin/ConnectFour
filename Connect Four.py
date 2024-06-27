import random, pygame, sys, time
from pygame.locals import *

#             NOTES
# - We want to make it so the user can play their piece by clicking on a row - In Turn()
# 



#Pygame Stuff
pygame.init()
clock = pygame.time.Clock()
resolution = (800, 900)
screen = pygame.display.set_mode(resolution)

board_rect = pygame.Rect(0,0,800,800)

board_pic = pygame.image.load("Connect4Board.png").convert()
board_img = pygame.transform.scale(board_pic, (800, 850))

c_rect = pygame.Rect(365,5,74,74)
c_surf = pygame.surface.Surface((74,74))
c_surf.fill((255,255,255))

font = pygame.font.Font(None, 64)

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
        #print('col full')
        #Turn(FP)
        pass

def Turn(FP) :
    #num = int(input('Which col? '))
    #print piece on top on screen based on turn
    #
    num = int(random.randint(1,7)) # - Change to pick
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

def PygameLoop(FP, end=False) :
    keys = pygame.key.get_pressed()
    num = None
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
        if keys[pygame.K_1]:
            num = 1
        if keys[pygame.K_2]:
            num = 2
        if keys[pygame.K_3]:
            num = 3
        if keys[pygame.K_4]:
            num = 4
        if keys[pygame.K_5]:
            num = 5
        if keys[pygame.K_6]:
            num = 6
        if keys[pygame.K_7]:
            num = 7

    screen.blit(board_img,board_rect)
    screen.blit(c_surf,c_rect)
    if FP :
        yellow = 0
        text = 'Yellow Won!'
    else :
        yellow = 255
        text = 'Red Won!'
    if end :
        win = font.render(text, False, (0,0,0))
        win_rect = win.get_rect()
        win_rect.center = (400,35)
        pygame.draw.circle(c_surf, (255,255,255), [37,37], 37, 0)
        screen.blit(win,win_rect.topleft)
    else :
        pygame.draw.circle(c_surf, (255,yellow,0), [37,37], 37, 0) #c_init
    #pygame.draw.circle(screen, (255,0,0), [100,762], 45, 0)
    #pygame.draw.circle(screen, (255,255,0), [200,250], 45, 0)
    ConvertBoard()
    pygame.display.flip()
    clock.tick(60)
    return num


def Play() :
    FP = True
    GameEnd = False
    GenBoard()
    #PrintBoard()
    while not GameEnd :
        #time.sleep(0.5) # - For looks
        #ColNum = Turn(FP)
        ColNum = PygameLoop(FP)
        if ColNum != None :
            PlayPiece(Col(ColNum), FP)
            if CheckWin(FP, ColNum) :
                GameEnd = True

            if FP :
                FP = False
            else :
                FP = True
    while True:
        PygameLoop(FP,True)

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

import pygame
import sys
import time
from pygame.locals import *


# Pygame Initialization
pygame.init()
clock = pygame.time.Clock()
resolution = (800, 900)
screen = pygame.display.set_mode(resolution)

# Sounds
chip_sound = pygame.mixer.Sound("chip_sound.wav")
winning_sound = pygame.mixer.Sound("winning_sound.wav")
pygame.mixer.music.load('BackgroundMusic.mp3')

def play_background_music(loop=True):
    if loop:
        pygame.mixer.music.play(-1)

play_background_music()

# Rects
board_rect = pygame.Rect(0, 0, 800, 800)

board_pic = pygame.image.load("Connect4Board.png").convert()
board_img = pygame.transform.scale(board_pic, (800, 850))

exit_pic = pygame.image.load("Exit.png").convert()
exit_img = pygame.transform.scale(exit_pic, (100, 30))
exit_rect = exit_img.get_rect()
exit_rect.topleft = (0, 16)

restart_pic = pygame.image.load("Restart.png").convert()
restart_img = pygame.transform.scale(restart_pic, (50, 50))
restart_rect = restart_img.get_rect()
restart_rect.topright = (780,25)



c_rect = pygame.Rect(365, 5, 74, 74)
c_surf = pygame.surface.Surface((74, 74))
c_surf.fill((255, 255, 255))

font = pygame.font.Font(None, 64)

#current_rect = pygame.Rect(70, 70, 47, 47)
#current_surf = pygame.Surface((47, 47), pygame.SRCALPHA)

def main():
    screen.blit(board_img, board_rect)
    screen.blit(c_surf, c_rect)
    pygame.draw.circle(c_surf, (255, 0, 0), [37, 44], 20, 0)
    screen.blit(exit_img, exit_rect)
    while True:
        Play()

def Col(Num):
    return {
        1: Col1,
        2: Col2,
        3: Col3,
        4: Col4,
        5: Col5,
        6: Col6,
        7: Col7
    }[Num]

def GenBoard():
    global Board, Col1, Col2, Col3, Col4, Col5, Col6, Col7
    Board = []
    Col1, Col2, Col3, Col4, Col5, Col6, Col7 = [], [], [], [], [], [], []
    for i in range(1, 8):
        GenBlankCol(Col(i))

def GenBlankCol(Col):
    for _ in range(7):
        Col.append('*')
    Board.append(Col)

def Piece(FP):
    return 'X' if FP else 'O'

def NotFullCol(Col):
    return '*' in Col

def PlayPiece(Col, ColNum, FP):
    if NotFullCol(Col):
        MovePiece(ColNum,Col.index('*'),FP)
        Col[Col.index('*')] = Piece(FP)
        screen.blit(board_img, board_rect)
        screen.blit(c_surf, c_rect)
        screen.blit(exit_img, exit_rect)
        return True
    return False

def MovePiece(Col,Row,FP) :
    width = Col * 100 - 50
    height = 730 - (Row * 102)
    move_times = round((height - 70)/10)
    current_rect = pygame.Rect(width, 70, 100, 100)
    current_surf = pygame.Surface((100, 100), pygame.SRCALPHA)
    for i in range(move_times) :
        current_rect = current_rect.move(0,10)
        time.sleep(0.007)
        screen.blit(board_img, board_rect)
        screen.blit(c_surf, c_rect)
        screen.blit(exit_img, exit_rect)
        ConvertBoard()
        screen.blit(current_surf, current_rect)
        if FP :
            yellow = 0
        else :
            yellow = 255
        pygame.draw.circle(current_surf, (255, yellow, 0), [50, 50], 47, 0)
        pygame.display.flip()

def CheckHoriWin(FP):
    WinCon = 0
    for C in range(1, 8):
        WinCon = 0
        for P in Col(C):
            if P == Piece(FP):
                WinCon += 1
                if WinCon >= 4:
                    winning_sound.play()
                    print(Piece(FP) + ' Won')
                    return True
            else:
                WinCon = 0

def CheckVirtWin(FP):
    WinCon = 0
    for R in range(7):
        WinCon = 0
        for C in range(1, 8):
            if Col(C)[R] == Piece(FP):
                WinCon += 1
                if WinCon >= 4:
                    winning_sound.play()
                    print(Piece(FP) + ' Won')
                    return True
            else:
                WinCon = 0

def CheckDiaWin(FP):
    if LtoRCheck(Piece(FP)):
        return True
    if RtoLCheck(Piece(FP)):
        return True

def LtoRCheck(P):
    WinNum = 0
    for C in range(1, 5):
        for S in range(4):
            WinNum = 0
            for i in range(4):
                if P == Col(C + i)[S + i]:
                    WinNum += 1
                    if WinNum >= 4:
                        winning_sound.play()
                        print(P + ' WON')
                        return True
                else:
                    WinNum = 0

def RtoLCheck(P):
    WinNum = 0
    for C in range(1, 5):
        for S in range(3, 7):
            WinNum = 0
            for i in range(4):
                if S - i >= 0 and P == Col(C + i)[S - i]:
                    WinNum += 1
                    if WinNum >= 4:
                        winning_sound.play()
                        print(P + ' WON')
                        return True
                else:
                    WinNum = 0

def CheckWin(FP):
    if CheckHoriWin(FP):
        return True
    if CheckVirtWin(FP):
        return True
    if CheckDiaWin(FP):
        return True

def PygameLoop(FP, end=False):
    keys = pygame.key.get_pressed()
    num = None
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
            sys.exit(0)
        if keys[pygame.K_1]:
            num = 1
            chip_sound.play()
        if keys[pygame.K_2]:
            num = 2
            chip_sound.play()
        if keys[pygame.K_3]:
            num = 3
            chip_sound.play()
        if keys[pygame.K_4]:
            num = 4
            chip_sound.play()
        if keys[pygame.K_5]:
            num = 5
            chip_sound.play()
        if keys[pygame.K_6]:
            num = 6
            chip_sound.play()
        if keys[pygame.K_7]:
            num = 7
            chip_sound.play()

        pos = pygame.mouse.get_pos()
        if exit_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            sys.exit(0)
        elif restart_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            return 'restart'

    screen.blit(board_img, board_rect)
    screen.blit(c_surf, c_rect)
    screen.blit(exit_img, exit_rect)

    if FP:
        yellow = 0
        text = 'Yellow Won!'
    else:
        yellow = 255
        text = 'Red Won!'

    if end:
        win = font.render(text, False, (0, 0, 0))
        win_rect = win.get_rect()
        win_rect.center = (400, 55)
        pygame.draw.circle(c_surf, (255, 255, 255), [37, 44], 20, 0)
        screen.blit(win, win_rect.topleft)
        screen.blit(restart_img, restart_rect)
    else:
        pygame.draw.circle(c_surf, (255, yellow, 0), [37, 44], 20, 0)
    

    ConvertBoard()
    pygame.display.flip()
    clock.tick(60)
    return num

def Play():
    FP = True
    GameEnd = False
    GenBoard()
    while not GameEnd:
        ColNum = PygameLoop(FP)
        if ColNum != None:
            if PlayPiece(Col(ColNum), ColNum, FP):
                if CheckWin(FP):
                    GameEnd = True
                FP = not FP
    while True:
        result = PygameLoop(FP, True)
        if result == 'restart':
            break

def ConvertBoard():
    for R in range(7):
        for C in range(1, 8):
            width = C * 100
            height = 765 - (R * 102)
            if Col(C)[R] == 'X':
                pygame.draw.circle(screen, (255, 0, 0), [width, height], 47, 0)
            elif Col(C)[R] == 'O':
                pygame.draw.circle(screen, (255, 255, 0), [width, height], 47, 0)

main()
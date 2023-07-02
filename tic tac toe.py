import tkinter
import pygame
import time
import random
pygame.init()
pygame.mixer.init()
diswid=500
disheig=600
list_x=[0,0,0,0,0,0,0,0,0]
list_o=[0,0,0,0,0,0,0,0,0]
k=0
draw=0
black=((0,0,0))
white=((255,255,255))
red=((255,0,0))
display=pygame.display.set_mode((diswid,disheig))
pygame.display.set_caption('tic tac toe game')
clock=pygame.time.Clock()
tic_toc_toe_board=pygame.image.load('tic_tac_toe_board.png')
tic_x=pygame.image.load('tic_x.png')
tic_o=pygame.image.load('tic_o.png')
#success=pygame.mixer.Sound('success.mp3')
#game_winning_claps=pygame.mixer.Sound('game_winning.wav')
def board(x,y):
    display.blit(tic_toc_toe_board,(x,y))
def tic_xs(x,y):
    display.blit(tic_x,(x,y))
def tic_os(x,y):
    display.blit(tic_o,(x,y))
def player_msg(text):
    font=pygame.font.SysFont('Algerian',50)
    textSurface=font.render(text,True,white,black)
    textwid,text_heig=font.size(text)
    a=(diswid//2)-(textwid//2)
    b=(disheig//2)-(text_heig//2)
    display.blit(textSurface,(150,20))
    
    pygame.display.flip()
def winning_msg(text):
    
    font=pygame.font.SysFont('Algerian',50)
    textSurface=font.render(text,True,white,black)
    textwid,text_heig=font.size(text)
    a=(diswid//2)-(textwid//2)
    b=(disheig//2)-(text_heig//2)
    display.blit(textSurface,(a,b))
    
    pygame.display.flip()
   
   
lis1=[1,1,1]
lis2=[1,1,1]

gameover=False
while not gameover:
    display.fill((0,0,0))
    for event in pygame.event.get():
          
        if event.type==pygame.QUIT:
            gameover=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
             v=True
             select_x,select_y=pygame.mouse.get_pos()
            
             if k%2==0:
                
                if select_x>32 and select_x<180 and select_y>98 and select_y<234:
                    list_x[0]=1
                elif select_x>186 and select_x<332 and select_y>98 and select_y<234:
                    list_x[1]=1
                elif select_x>336 and select_x<481 and select_y>98 and select_y<234:
                    list_x[2]=1
                elif select_x>32 and select_x<180 and select_y>234 and select_y<368:
                    list_x[3]=1
                elif select_x>186 and select_x<332 and select_y>234 and select_y<368:
                    list_x[4]=1
                elif select_x>336 and select_x<481 and select_y>234 and select_y<368:
                    list_x[5]=1
                elif select_x>32 and select_x<180 and select_y>371 and select_y<500:
                    list_x[6]=1
                elif select_x>186 and select_x<332 and select_y>371 and select_y<500:
                    list_x[7]=1
                elif select_x>336 and select_x<481 and select_y>371 and select_y<500:
                    list_x[8]=1
                else:
                    k=k-1
                    print("wrong choice")
                draw=draw+1
                
             else:
               
                if select_x>32 and select_x<180 and select_y>98 and select_y<234:
                    list_o[0]=1
                elif select_x>186 and select_x<332 and select_y>98 and select_y<234:
                    list_o[1]=1
                elif select_x>336 and select_x<481 and select_y>98 and select_y<234:
                    list_o[2]=1
                elif select_x>32 and select_x<180 and select_y>234 and select_y<368:
                    list_o[3]=1
                elif select_x>186 and select_x<332 and select_y>234 and select_y<368:
                    list_o[4]=1
                elif select_x>336 and select_x<481 and select_y>234 and select_y<368:
                    list_o[5]=1
                elif select_x>32 and select_x<180 and select_y>371 and select_y<500:
                    list_o[6]=1
                elif select_x>186 and select_x<332 and select_y>371 and select_y<500:
                    list_o[7]=1
                elif select_x>336 and select_x<481 and select_y>371 and select_y<500:
                    list_o[8]=1
                else:
                    k=k-1
                    print("wrong choice")
                draw=draw+1
             #success.play()
             k=k+1
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_axis=-10
            elif event.key==pygame.K_RIGHT:
                x_axis=10
            elif event.key==pygame.K_UP:
                v=True
    board(-25,10)
    
    list_x1=list_x[0:3]
    list_x2=list_x[3:6]
    list_x3=list_x[6:9]          
    list_x4=list_x[0:7:3]
    list_x5=list_x[1:8:3]
    list_x6=list_x[2:9:3]
    list_x7=list_x[0:9:4]
    list_x8=list_x[2:8:2]
    list_o1=list_o[0:3]
    list_o2=list_o[3:6]
    list_o3=list_o[6:9]          
    list_o4=list_o[0:7:3]
    list_o5=list_o[1:8:3]
    list_o6=list_o[2:9:3]
    list_o7=list_o[0:9:4]
    list_o8=list_o[2:8:2]
    
    if list_x[0]:
        tic_xs(16,66)
    if list_x[1]:
        tic_xs(170,66)
    if list_x[2]:    
        tic_xs(318,66)
    if list_x[3]:
        tic_xs(16,195)
    if list_x[4]:
        tic_xs(170,195)
    if list_x[5]:
        tic_xs(318,195)
    if list_x[6]:
        tic_xs(16,315)
    if list_x[7]:
        tic_xs(170,315)
    if list_x[8]:
        tic_xs(318,315)
    if list_o[0]:
        tic_os(16,76)
    if list_o[1]:
        tic_os(170,76)
    if list_o[2]:    
        tic_os(318,76)
    if list_o[3]:
        tic_os(16,215)
    if list_o[4]:
        tic_os(170,215)
    if list_o[5]:
        tic_os(318,215)
    if list_o[6]:
        tic_os(16,345)
    if list_o[7]:
        tic_os(170,345)
    if list_o[8]:
        tic_os(318,345)
    if k%2==0:
        player_msg("player 1")
    else:
        player_msg("player 2")
    
    pygame.display.update()
    if (list_x1==lis1 or list_x2==lis1 or list_x3==lis1 or list_x4==lis1 or list_x5==lis1 or list_x6==lis1 or list_x7==lis1 or list_x8==lis1):
       winning_msg("PLAYER 1 WON")
       #game_winning_claps.play()
       time.sleep(3)
       #game_winning_claps.stop()
       list_x=[0,0,0,0,0,0,0,0,0]
       list_o=[0,0,0,0,0,0,0,0,0]
       k=0
       draw=0
    elif (list_o1==lis2 or list_o2==lis2 or list_o3==lis2 or list_o4==lis2 or list_o5==lis2 or list_o6==lis2 or list_o7==lis2 or list_o8==lis2):
       winning_msg("PLAYER 2 WON")
       #game_winning_claps.play()
       time.sleep(3)
       #game_winning_claps.stop()
       list_x=[0,0,0,0,0,0,0,0,0]
       list_o=[0,0,0,0,0,0,0,0,0]
       draw=0
       k=0
    elif draw==9 and (list_x!=list_o):
       winning_msg("Draw match")
       time.sleep(3)
       list_x=[0,0,0,0,0,0,0,0,0]
       list_o=[0,0,0,0,0,0,0,0,0]
       k=0
       draw=0
       
pygame.quit()
quit()

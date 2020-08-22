from pygame import image, display, event, draw
import pygame
import os 
import game_confi as gc 
import model
from time import sleep

def get_cord(row, col):
    
    if row == 0 :
        yl = 330
    elif row ==1:
        yl = 570
    else:
        yl = 810

    if col == 0:
        xl = 120
    elif col == 1 :
        xl = 490
    else:
        xl = 880
    return xl,yl


def cancel(n):
    if n == 1:
        draw.line(screen, (255,0,100), (60, 415) , (1110, 415), 10)
    elif n == 2 :
        draw.line(screen, (255,0,100), (60, 660) , (1110, 660), 10)
    elif n == 3:
        draw.line(screen, (255,0,100), (60, 900) , (1110, 900), 10)

    elif n == 4:
        draw.line(screen, (255,0,100), (200, 300) , (200, 1010), 10)
    elif n == 5 :
        draw.line(screen, (255,0,100), (570, 300) , (570, 1010), 10)
    elif n ==6 :
        draw.line(screen, (255,0,100), (960, 300) , (960, 1010), 10)
    
    elif n == 7:
        draw.line(screen, (255,0,100), (60 , 340) , (1070 , 980), 10)
        
    else:
        draw.line(screen, (255,0,100), (60, 980) , (1070, 340), 10)



pygame.init()
display.set_caption('tic-tac-toe')
screen = display.set_mode((1178,1200))
#screen.fill((255,0,0))
screen.blit(gc.background,(0,0))



display.flip()
go = True
running = True
while running:
    #screen.blit(gc.background,(0,0))
    events = event.get()
    if model.arr == []:
        model.initial()
        screen.blit(gc.draw,(180,450))
        display.flip()
        sleep(.5)
        print('draw')
        screen.blit(gc.background,(0,0))
        display.flip()
        continue
        
        
    for e in events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEMOTION:
            x,y = pygame.mouse.get_pos()
            #print(x, y)

        if e.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
           
            if 60 <= x <= 1108 and 300 <= y <= 980 :
                row,col = model.row_col(x, y)
                #print(row, col)
                if model.empty(row, col):
                    #print('in')
                    xl,yl = get_cord(row,col)
                    screen.blit(gc.o,(xl,yl)) 
                    display.flip()
                    #sleep(0.2)
                    if model.match(model.user)[0]:
                        print('You Won !!!')
                        cancel(model.match(model.user)[1])
                        display.flip()
                        sleep(1)
                        screen.blit(gc.win,(240,450))
                        display.flip()
                        sleep(.5)
                        model.initial()
                        screen.blit(gc.background,(0,0))
                        go = False

                    elif go and model.arr != []:
                        index = model.comp_turn(model.get_combs(model.user,model.comp))
                        
                        x_comp , y_comp = get_cord(index // 3, index % 3)
                        screen.blit(gc.x,(x_comp, y_comp)) 
                       

                    if  go and model.match(model.comp)[0]:
                        print('You Lost :(')
                        cancel(model.match(model.comp)[1])
                        display.flip()
                        sleep(.2)
                        screen.blit(gc.lost,(240,450))
                        display.flip()
                        sleep(.5)
                        model.initial()
                        
                        screen.blit(gc.background,(0,0))
                        
                    go = True
                    print('arr :' , model.arr , 'user :' , model.user, '   comp :', model.comp)
                    display.flip()

                    
    
 
'''
Author: Marcela Estrada
'''

import sys, pygame

pygame.init()

screen_size = 500,500

screen = pygame.display.set_mode(screen_size)
grass = pygame.image.load("images/grass.png")
chicken_r = [pygame.image.load("images/chicken/r_walk1.png"),pygame.image.load("images/chicken/r_walk2.png"),pygame.image.load("images/chicken/r_walk3.png")]
chicken_l = [pygame.image.load("images/chicken/l_walk1.png"),pygame.image.load("images/chicken/l_walk2.png"),pygame.image.load("images/chicken/l_walk3.png")]

clock = pygame.time.Clock()
fps = 7
black = 0,0,0
vel = 30
dir = True
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(grass,(0,0))
    if dir == True:
        screen.blit(chicken_r[0],(vel,0))
    else:
        screen.blit(chicken_l[0],(vel,0))
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_RIGHT]):
        screen.blit(grass,(0,0))
        dir = True
        vel+=1
        if(vel%2 == 0):
            screen.blit(chicken_r[0],(vel,0))
        else:
            screen.blit(chicken_r[2],(vel,1))
    if(keys[pygame.K_LEFT]):
        screen.blit(grass,(0,0))
        dir = False
        vel-=1
        if(vel%2 == 0):
            screen.blit(chicken_l[1],(vel,0))
        else:
            screen.blit(chicken_l[2],(vel,1))
    

    clock.tick(fps)
    pygame.display.flip()


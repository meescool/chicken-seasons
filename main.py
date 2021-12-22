'''
Author: Marcela Estrada
'''

import sys, pygame
import chicken as ch

pygame.init()

screen_size = 500,500

screen = pygame.display.set_mode(screen_size)
grass = pygame.image.load("images/grass.png")
chicken_r = [pygame.image.load("images/chicken/r_walk1.png"),pygame.image.load("images/chicken/r_walk2.png"),pygame.image.load("images/chicken/r_walk3.png")]
chicken_l = [pygame.image.load("images/chicken/l_walk1.png"),pygame.image.load("images/chicken/l_walk2.png"),pygame.image.load("images/chicken/l_walk3.png")]
chicken_u = [pygame.image.load("images/chicken/u_walk1.png"),pygame.image.load("images/chicken/u_walk2.png"),pygame.image.load("images/chicken/u_walk3.png")]
chicken_d = [pygame.image.load("images/chicken/d_walk1.png"),pygame.image.load("images/chicken/d_walk2.png"),pygame.image.load("images/chicken/d_walk3.png")]

clock = pygame.time.Clock()
fps = 7
black = 0,0,0
chicken= {
    'img':chicken_r[0],
    'x':50,
    'y':50,
    'dir':[50,50]
}
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(grass,(0,0))
        
    keys = pygame.key.get_pressed()
    chicken = ch.moveChicken(keys, chicken,chicken_r,chicken_l,chicken_u,chicken_d)
    screen.blit(chicken['img'],chicken['dir'])

    clock.tick(fps)
    pygame.display.flip()


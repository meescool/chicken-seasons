import sys, pygame
def moveChicken(keys,chicken,right,left,up,down):
    
    if(keys[pygame.K_RIGHT]):
        chicken['x']+=3
        if(chicken['x']%2 == 0):
            chicken['img'] = right[1]
            chicken['dir'] = [chicken['x'],chicken['y']]
        else:
            chicken['img'] = right[2]
            chicken['dir'] = [chicken['x'],chicken['y']+1]
    if(keys[pygame.K_LEFT]):
        chicken['x']-=3
        if(chicken['x']%2 == 0):
            chicken['img'] = left[1]
            chicken['dir'] = [chicken['x'],chicken['y']]
        else:
            chicken['img'] = left[2]
            chicken['dir'] = [chicken['x'],chicken['y']+1]
    
    if(keys[pygame.K_UP]):
        chicken['y']-=3
        if(chicken['y']%2 == 0):
            chicken['img'] = up[0]
            chicken['dir'] = [chicken['x'],chicken['y']]
        else:
            chicken['img'] = up[1]
            chicken['dir'] = [chicken['x'],chicken['y']]

    if(keys[pygame.K_DOWN]):
        chicken['y']+=3
        if(chicken['y']%2 == 0):
            chicken['img'] = down[0]
            chicken['dir'] = [chicken['x'],chicken['y']]
        else:
            chicken['img'] = down[1]
            chicken['dir'] = [chicken['x'],chicken['y']]
    return chicken
    
    
    
import pygame, sys
from pygame.locals import *



def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,500),0,32)
    windowSurface = pygame.display.set_mode((500, 500), pygame.DOUBLEBUF)
    WHITE=(255,255,255)
    blue=(0,0,255)
    black=(1,1,1)

    DISPLAY.fill(WHITE)


    pygame.draw.rect(DISPLAY, blue, (0, 150, 500, 400))
    pygame.draw.rect(DISPLAY, black, (200, 100, 150, 120)) # Change 2nd number, the lower than 150 float, after 150 sink
    s = pygame.Surface((1000, 750), pygame.SRCALPHA)  # per-pixel alpha
    s.fill((255, 255, 255, 128))  # notice the alpha value in the color
    windowSurface.blit(s, (0, 150))

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main ()
import pygame, sys
from pygame.locals import *
import calcuations


def main():
    pygame.init()

    volumeo=2.0
    densityl=2.0
    mass=3.0
    densityo=calcuations.getdensity(mass, volumeo)
    print densityo

    DISPLAY=pygame.display.set_mode((500,500),0,32)
    windowSurface = pygame.display.set_mode((500, 500), pygame.DOUBLEBUF)
    WHITE=(255,255,255)
    blue=(0,0,255)
    black=(1,1,1)

    DISPLAY.fill(WHITE)


    height_of_shape = 120
    surface = 150
    bottom_of_shape=surface-height_of_shape #Shape sitting ontop of surface

    volume_submerged = calcuations.volume_submerged(fluid_density=densityl, object_density=densityo, object_volume=volumeo)


    if densityl > densityo:
        print "floating"
        bottom_of_shape = bottom_of_shape + height_of_shape * calcuations.fraction_submerged(volume_submerged=volume_submerged, object_volume=volumeo)
    elif densityo > densityl:
        print "sinking"
        bottom_of_shape = 380
    print densityo

    #bottom_of_shape = bottom_of_shape + height_of_shape*densityo

    pygame.draw.rect(DISPLAY, blue, (0, surface, 500, 400))
    pygame.draw.rect(DISPLAY, black, (200, bottom_of_shape, 150, height_of_shape)) # Change 2nd number, the lower than 150 float, after 150 sink
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
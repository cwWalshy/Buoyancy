import pygame
from pygame.locals import *
import calcuations
from Tkinter import *

def update_mass(val):
    global mass
    mass = float(val)
    print val

def update_volumeo(val):
    global volumeo
    volumeo = float(val)
    print val

def main():
    pygame.init()

    master = Tk() #Sets up the slider for setting the value of the mass and volume
    w = Scale(master, from_=1.0, to=10.0, command=update_mass)


    w.label = Label(master, text="This scale changes the Mass of the object (Vertical Scale)")
    w.label.pack()

    print ("w", w.get())

    w.pack()

    w = Scale(master, from_=1.0, to=10.0, orient=HORIZONTAL, command=update_volumeo)

    w.label = Label(master, text="This scale changes the Volume of the object (Horizontal Scale)")
    w.label.pack()


    print w
    w.pack()
    mainloop()

    densityl = 1.0
    densityo = calcuations.getdensity(mass, volumeo)
    print mass, "kg, is the mass of the object"
    print volumeo, "10cm^3, is the volume of the object"
    print densityo, "kg/L is the density of the object"

    DISPLAY=pygame.display.set_mode((500,500),0,32) #Sets up the graphics of the map
    windowSurface = pygame.display.set_mode((500, 500), pygame.DOUBLEBUF)
    WHITE=(255,255,255)
    blue=(0,0,255)
    black=(1,1,1)

    DISPLAY.fill(WHITE)


    height_of_shape = 120
    surface = 150
    bottom_of_shape=surface-height_of_shape #Shape sitting ontop of surface

    volume_submerged = calcuations.volume_submerged(fluid_density=densityl, object_density=densityo, object_volume=volumeo)

    if densityo == densityl:
        print "Object has a neutral buoyancy" #the shape will sit just below the surface of the water
        bottom_of_shape = bottom_of_shape + height_of_shape
    elif densityl > densityo:
        print "Object is floating" #Object is floating on/near the surface of the water
        bottom_of_shape = bottom_of_shape + height_of_shape * calcuations.fraction_submerged(volume_submerged=volume_submerged, object_volume=volumeo)
    elif densityo > densityl:
        print "Object is sinking" #Object is sitting at the bottom of the window completely sunk
        bottom_of_shape = 380

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
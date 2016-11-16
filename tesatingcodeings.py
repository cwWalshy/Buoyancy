import sys, pygame
pygame.init()

size = width, height = 320, 240
black = (0, 0, 0)
red = (255, 0, 0)
pygame.display.set_caption("Object Move Test")
clock = pygame.time.Clock()

def main():
    screen = pygame.display.set_mode(size)
    shape = pygame.draw.rect(screen, (255, 0, 0), (200, 100, 10, 10,))
    ballrect = pygame.Surface((10,10), 0, shape)

    def checkKeys(speedY, speedX, shape):
        key = pygame.key
        pygame.event.pump()
        if key.get_pressed()[pygame.K_UP] and speedY < 1:
            speedY = speedY - 1
            #print 'UP'
        if key.get_pressed()[pygame.K_DOWN] and speedY > -1:
            speedY = speedY + 1
            #print 'DOWN'
        if key.get_pressed()[pygame.K_LEFT] and speedX > -1:
            speedX = speedX - 1
            #print 'LEFT'
        if key.get_pressed()[pygame.K_RIGHT] and speedX < 1:
            speedX = speedX + 1
            #print speedX
        speed = [speedX, speedY]
        #print speed
        moveShape(speed, shape)

    def moveShape(speed, shape):
        print speed
        shape.move_ip(speed)
        if shape.left < 0 or shape.right > width:
            speed[0] = -speed[0]
        if shape.top < 0 or shape.bottom > height:
            speed[1] = -speed[1]

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        speedX, speedY = (0, )*2
        speed = [speedX, speedY]
        screen.fill((255,255,255))
        clock.tick(40)
        checkKeys(speedX, speedY, shape)

        screen.blit(ballrect, shape)
        pygame.display.flip()

if __name__ == '__main__':
    main()
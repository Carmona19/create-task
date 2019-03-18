import pygame
import random

pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 800))
done = False
gameStatus = "playing"
pygame.display.set_caption('Galg.io')
restartTime = 0


#            (x, y, Speed, shoot     score
playership = [20,790,7,pygame.K_SPACE, 0]





def drawShip(playership):
    pointList = [(playership[0],playership[1]),(playership[0]+25,playership[1]-50),(playership[0]+50,playership[1])]
    pygame.draw.polygon(screen,(255,0,0),pointList,0)

def moveShip(playership):
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_d]:
        playership[0] += playership[2]
    if pressed[pygame.K_a]:
        playership[0] -= playership[2]


running = True
while not done:

    clock.tick(60)

    # loop through and empty the event queue, key presses, button clicks, etc.
    for event in pygame.event.get():

        # if the eventis a click on the "X" close button
        if event.type == pygame.QUIT:
            done = True
            running = False


    if gameStatus == "playing":
        playership[4] = 1
        drawShip(playership)
        moveShip(playership)




        
    pygame.display.flip()
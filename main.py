import pygame


pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 950))
done = False
gameStatus = "playing"
pygame.display.set_caption('Galg.io')

#            (x, y, Speed, left,   right        shoot         score
playership = [20,940,7,pygame.K_a, pygame.K_d,pygame.K_SPACE, 0]

def drawShip():
    pointList = [(playership[0],playership[1]),(playership[0]+25,playership[1]-50),(playership[0]+50,playership[1])]
    pygame.draw.polygon(screen,(255,0,0),pointList,0)

def moveShip():
    keypressed = pygame.key.get_pressed()
    # check right key for press
    if keypressed[playership[3]]:
        playership[0] -= playership[2]
    # check fpr left key being pressed
    if keypressed[playership[4]]:
        playership[0] += playership[2]

























running = True
while not done:

    clock.tick(60)

    # loop through and empty the event queue, key presses, button clicks, etc.
    for event in pygame.event.get():

        # if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            done = True
            running = False
        if event.type == pygame.K_SPACE:
            if gameStatus == "gameOver":
                playership[5] = 0

    if gameStatus == "playing":
        playership[5] = 1
        drawShip()
        moveShip()

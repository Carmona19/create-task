
import pygame  # needed to import the pygame framework

pygame.init()
screen = pygame.display.set_mode((900, 950))
clock = pygame.time.Clock()
done = False
gameStatus = "playing"

pygame.display.set_caption('Galg.io')
spaceship = pygame.image.load("spaceship.png")

x = 0;  # x coordnate of image
y = 850;  # y coordinate of image
screen.blit(spaceship, (x, y))  # paint to screen
pygame.display.flip()  # paint screen one time]


#            (x, y, Speed, left,   right   score
playership = [0,850,7,pygame.K_d, pygame.K_a, 0]



boundaries = [ pygame.Rect(400,300,170,35)]



def drawMap(boundaries):
    for i in range (0,len(boundaries),1):
        pygame.draw.rect(screen, (15,140,30),boundaries[i], 0)


def drawPlayer(playership):
        pygame.draw.circle(screen,
                           (255,25,40),
                           (playership[0], playership[1]),
                           17)

def checkPlayerInput(playership):
    hitbox = pygame.Rect(playership[0] - 17, playership[1] - 17, 34, 34)
    oldx = playership[0]
    oldy = playership[1]

    collison = checkForCollision(playership, boundaries)
    if collison == True:
        playership[0] = oldx
        playership[1] = oldy
    # keep player on screen
    playerOffScreen = isPlayerOffScreen(playership)
    if playerOffScreen == True:
        playership[0] = oldx
        playership[1] = oldy

def isPlayerOffScreen(playership):
    if playership[0] < 17:
        return True
    if playership[0] > 1200 - 17:
        return True
    if playership[1] < 17:
        return True
    if playership[1] > 900 - 17:
        return True

    return False

def moveship(player):
    keypressed = pygame.key.get_pressed()
    if keypressed[player[4]]:
        player[0] -= player[2]
    # check fpr UP key being pressed
    if keypressed[player[3]]:
        player[0] += player[2]

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

    if gameStatus == "playting":


        drawMap(boundaries)
        drawPlayer(playership)


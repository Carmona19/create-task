import pygame
import random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 800))
done = False
gameStatus = "playing"
pygame.display.set_caption('Galg.io')
restartTime = 0
myFont = pygame.font.SysFont('Comic Sans MS', 100)
myFontTimer = pygame.font.SysFont('Comic Sans MS', 25)
myFontScore = pygame.font.SysFont('Comic Sans MS', 25)
timer = pygame.time.get_ticks()
enemnyCounter = []

#            (x, y, Speed, shoot     score
playership = [20, 790, 7, pygame.K_SPACE, 0]

downEnemies = []


def drawShip(playership):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 900, 800), 0)

    pointList = [(playership[0], playership[1]), (playership[0] + 25, playership[1] - 50),
                 (playership[0] + 50, playership[1])]
    pygame.draw.polygon(screen, (150, 0, 181), pointList, 0)

    screenText = myFontTimer.render("Time " + str(((pygame.time.get_ticks()) - restartTime) / 1000), False,
                                    (255, 255, 255))
    screen.blit(screenText, (400, 10))


# (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def moveShip(playership):

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_d]:
        playership[0] += playership[2]

    if pressed[pygame.K_a]:
        playership[0] -= playership[2]



def initEnemies():
    global downEnemies
    downEnemies.append(pygame.Rect(150, -50, 25, 25))
    downEnemies.append(pygame.Rect(200, -50, 25, 25))
    downEnemies.append(pygame.Rect(250, -50, 25, 25))


def drawEnemies():
    for enemy in downEnemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)


def moveEnemies():
    for enemy in downEnemies:
        enemy.y += 3
        if enemy.y > 800:
            enemy.y = -50
            enemy.x = random.randint(0, 780)
        if enemy.x<playership[0]:
            enemy.x += 3
        else:
            enemy.x -= 3


def checkForCollisions():
    global downEnemies
    global gameStatus
    pointList = [(playership[0], playership[1]), (playership[0] + 25, playership[1] - 50),
                 (playership[0] + 50, playership[1])]
    for enemy in downEnemies:
        if enemy.colliderect(pygame.draw.polygon(screen, (150, 0, 181), pointList, 0)):
            gameStatus = "Gameover"


def resetGame():
    global lastRestartTime

    resetEnemies()
    initEnemies()


def Updatescore():
    global gameStatus
    if gameStatus == "playing":
        playership[4] = str(((pygame.time.get_ticks()) - restartTime) / 1000)


def displayScore():
    textScoreSurface = myFontScore.render("Your Score: " + str(playership[4]),
                                          False,
                                          (255, 255, 255))
    screen.blit(textScoreSurface, (400, 400))


def drawGameOver():
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 900, 800), 0)

    textSurface = myFont.render("Gameover  ", False, (255, 255, 255))
    screen.blit(textSurface, (250, 10))


initEnemies()
running = True
while not done:

    clock.tick(30)

    # loop through and empty the event queue, key presses, button clicks, etc.
    for event in pygame.event.get():

        # if the eventis a click on the "X" close button
        if event.type == pygame.QUIT:
            done = True
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gameStatus == "Gameover":
                    resetGame()
                    gameStatus = "playing"

    if gameStatus == "playing":

        drawShip(playership)
        drawEnemies()
        moveShip(playership)
        moveEnemies()
        checkForCollisions()
        Updatescore()
    elif gameStatus == "Gameover":
        drawGameOver()
        displayScore()

    pygame.display.flip()
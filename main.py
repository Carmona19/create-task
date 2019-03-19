import pygame
import random

pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 800))
done = False
gameStatus = "playing"
pygame.display.set_caption('Galg.io')
restartTime = 0
myFont = pygame.font.SysFont('Comic Sans MS', 30)

#            (x, y, Speed, shoot     score
playership = [20,790,7,pygame.K_SPACE, 0]

downEnemies = []



def drawShip(playership):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 900, 800), 0)

    pointList = [(playership[0],playership[1]),(playership[0]+25,playership[1]-50),(playership[0]+50,playership[1])]
    pygame.draw.polygon(screen,(150, 0, 181) ,pointList,0)
# (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def moveShip(playership):
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_d]:
        playership[0] += playership[2]
    if pressed[pygame.K_a]:
        playership[0] -= playership[2]

def initEnemies():
    global downEnemies
    downEnemies.append(pygame.Rect(200, -50, 25, 25))

def drawEnemies():
    for enemy in downEnemies:
        pygame.draw.rect(screen,(255,0,0), enemy)

def moveEnemies():
    for enemy in downEnemies:
        enemy.y += 3
        if enemy.y > 800:
            enemy.y = -50
            enemy.x = random.randint(0,780)

def checkCollisions():
    global downEnemies
    global gameStatus
    for enemy in downEnemies:
        if enemy.colliderect(pygame.Rect(pygame.Rect(playership[0],playership[1],25,25))):
            gameStatus = "Gameover"

def drawGameOver():
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 900, 800), 0)

            textSurface = myFont.render("Gameover  ", False, (255, 255, 255))
            screen.blit(textSurface, (330, 10))






initEnemies()
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
        drawEnemies()
        moveShip(playership)
        moveEnemies()
        checkCollisions()
    elif gameStatus == "Gameover":
        drawGameOver()




        
    pygame.display.flip()
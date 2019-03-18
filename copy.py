import pygame #needed to import the pygame framework
import random
#initializes all the modules required for PyGame
pygame.init()
pygame.font.init()
pygame.mixer.init()
#launch a window of the desired size, screen equals a Surface which is an object
#we can perform graphical operations on. Think of a Surface as a blank piece of paper
screen = pygame.display.set_mode((800, 600))

#variable to control the game loop, keeps our code running until we flip it to True
done = False
gameStatus = "playing"
finalScore = 0



_songs = ['YNW Melly - Mixed Personalities (ft. Kanye West) [Official Audio].mp3', 'oro solido - se encendio el beeper.(1999).mp3', 'blueface - Thotiana.mp3', 'Roddy Ricch - Die Young (Lyrics).mp3', 'Lil Keed - Nameless [Official Video].mp3', 'Lil TJay - Goat (Music Video) [Shot by Ogonthelens].mp3', 'Baila Baila Baila.mp3', 'Anuel AA, Karol G - Secreto.mp3','German.mp3','Juls Bad Ft Not3s , Kojo Funds ,Eugy.mp3']
_currently_playing_song = None
SONG_END = pygame.USEREVENT + 1


upCount = 0
rightCount = 0
leftCount = 0
downCount = 0

#player variables
x = 400
y = 300
size = 15
speed = 7
color = (255, 255, 255)
bomb = 1

# List of enemies
downEnemies = []
rightEnemies = []
leftEnemies = []
upEnemies = []

timer = pygame.time.get_ticks()
lastRestartTime = 0
myFont = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()
enemySpeed = 2


def play_a_different_song():
    global _currently_playing_song
    global _songs
    next_song = random.choice(_songs)
    while next_song == random.choice(_songs):
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

def handlePlayerinput():
    global x
    global y
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_d]:
        x += speed
    if pressed[pygame.K_a]:
        x -= speed
    if pressed[pygame.K_w]:
        y -= speed
    if pressed[pygame.K_s]:
        y += speed


def powerUp():
    global bomb
    global textSurface
    textSurface = myFont.render("Bombs = " + str(bomb), False, (255, 255, 255))
    screen.blit(textSurface, (540, 10))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            if bomb > 0:
                clearEnemies()
                initEnemies()
                bomb -= 1



def resetCount():
    global upCount
    global rightCount
    global leftCount
    global downCount
    upCount = 0
    rightCount = 0
    leftCount = 0
    downCount = 0


def draw():
    global x
    global y
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 800, 600), 0)

    pygame.draw.rect(screen, color, pygame.Rect(x,y,size,size))

    drawEnemies()

    textSurface = myFont.render("Time " + str(((pygame.time.get_ticks())-lastRestartTime)/1000), False, (255,255,255))
    screen.blit(textSurface, (350,10))



    if x > 780:
        x = 780
    if x < 5:
        x = 5
    if y > 580:
        y = 580
    if y < 5:
        y = 5

def initEnemies():
    global downEnemies
    global rightEnemies
    global upEnemies
    global leftEnemies

    rightEnemies.append(pygame.Rect(-50, 400, 20, 20))
    rightEnemies.append(pygame.Rect(-50, 70, 20, 20))
    rightEnemies.append(pygame.Rect(-100, 100, 20, 20))
    rightEnemies.append(pygame.Rect(-90, 200, 20, 20))
    #rightEnemies.append(pygame.Rect(-80, 600, 20, 20))
    #rightEnemies.append(pygame.Rect(-50, 500, 20, 20))

    downEnemies.append(pygame.Rect(200, -50, 20, 20))
    downEnemies.append(pygame.Rect(400, -60, 20, 20))
    downEnemies.append(pygame.Rect(300, -90, 20, 20))
    downEnemies.append(pygame.Rect(100, -100, 20, 20))
   # downEnemies.append(pygame.Rect(600, -50, 20, 20))
    #downEnemies.append(pygame.Rect(500, -50, 20, 20))

    upEnemies.append(pygame.Rect(100, 790, 20, 20))
    upEnemies.append(pygame.Rect(400, 750, 20, 20))
    upEnemies.append(pygame.Rect(300, 730, 20, 20))
    upEnemies.append(pygame.Rect(600, 700, 20, 20))
   # upEnemies.append(pygame.Rect(350, 730, 20, 20))
    #upEnemies.append(pygame.Rect(200, 700, 20, 20))

    leftEnemies.append(pygame.Rect(850, 40, 20, 20))
    leftEnemies.append(pygame.Rect(840, 100, 20, 20))
    leftEnemies.append(pygame.Rect(870, 230, 20, 20))
    leftEnemies.append(pygame.Rect(820, 540, 20, 20))
   # leftEnemies.append(pygame.Rect(830, 330, 20, 20))
    #leftEnemies.append(pygame.Rect(860, 440, 20, 20))




def drawEnemies():
    for enemy in downEnemies:
        pygame.draw.rect(screen,(255,0,0), enemy)
    for enemy in rightEnemies:
        pygame.draw.rect(screen, (0, 255, 0), enemy)
    for enemy in upEnemies:
        pygame.draw.rect(screen, (0, 255, 255), enemy)
    for enemy in leftEnemies:
        pygame.draw.rect(screen, (255, 0, 255), enemy)

def clearEnemies():
    global upEnemies
    global downEnemies
    global leftEnemies
    global rightEnemies
    upEnemies = []
    downEnemies = []
    rightEnemies = []
    leftEnemies = []



def resetGame():
    global lastRestartTime
    global  bomb
    clearEnemies()
    initEnemies()
    lastRestartTime = pygame.time.get_ticks()
    bomb = 1


def checkCollisions():
    global upEnemies
    global downEnemies
    global leftEnemies
    global rightEnemies
    global x
    global y
    global gameStatus
    global finalScore
    for enemy in downEnemies:
        if enemy.colliderect(pygame.Rect(pygame.Rect(x,y,size,size))):
            gameStatus = "Gameover"
            finalScore =  pygame.time.get_ticks() - lastRestartTime
    for enemy in upEnemies:
        if enemy.colliderect(pygame.Rect(pygame.Rect(x,y,size,size))):
            gameStatus = "Gameover"
            finalScore =  pygame.time.get_ticks() - lastRestartTime
    for enemy in leftEnemies:
        if enemy.colliderect(pygame.Rect(pygame.Rect(x,y,size,size))):
            gameStatus = "Gameover"
            finalScore =  pygame.time.get_ticks() - lastRestartTime
    for enemy in rightEnemies:
        if enemy.colliderect(pygame.Rect(pygame.Rect(x,y,size,size))):
            gameStatus = "Gameover"
            finalScore =  pygame.time.get_ticks() - lastRestartTime

def drawGameOver():
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 800, 600), 0)

    textSurface = myFont.render("Gameover  ", False,(255, 255, 255))
    screen.blit(textSurface, (330, 10))

    textSurface = myFont.render("Final Score " + str(finalScore), False, (255, 255, 255))
    screen.blit(textSurface, (300, 200))

    textSurface = myFont.render("Press Spacebar to play again.  " , False, (255, 255, 255))
    screen.blit(textSurface, (225, 250))



def moveEnemies():
    global downCount
    global upCount
    global leftCount
    global rightCount
    global downEnemies

    for enemy in downEnemies:
        enemy.y += 3
        if enemy.y > 600:
            enemy.y = -50
            enemy.x = random.randint(0,780)
            downCount += 1

            if downCount % 2 == 0:
                downEnemies.append(pygame.Rect(random.randint(0,780),random.randint(-100,-20), 20+downCount,20+downCount))
    for enemy in rightEnemies:
        enemy.x += 3
        if enemy.x > 800:
            enemy.x = -50
            enemy.y = random.randint(0,780)
            rightCount += 1

            if rightCount % 2 == 0:
                rightEnemies.append(pygame.Rect(random.randint(-100, -20),random.randint(0, 580), 20+rightCount,20+rightCount))
    for enemy in upEnemies:
        enemy.y -= 3
        if enemy.y < 20:
            enemy.x = random.randint(0,780)
            enemy.y = 650
            upCount += 1

            if upCount % 2 == 0:
                upEnemies.append(pygame.Rect(random.randint(0, 780), random.randint(-100, -20), 20 + upCount, 20 + upCount))
    for enemy in leftEnemies:
        enemy.x -= 3
        if enemy.x < -20:
            enemy.x = 800
            enemy.y = random.randint(0,580)
            leftCount += 1

            if leftCount % 2 == 0:
                leftEnemies.append(pygame.Rect(random.randint(-100, -20), random.randint(0, 580), 20 + leftCount, 20 + leftCount))


initEnemies()


play_a_different_song()
pygame.mixer.music.set_endevent(SONG_END)


#continually run the game loop until done is switch to True
while not done:

    clock.tick(60)
    #loop through and empty the event queue, key presses, button clicks, etc.
    for event in pygame.event.get():

        #if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gameStatus == "Gameover":
                    resetGame()
                    gameStatus = "playing"
                    x = 400
                    y = 300
        if event.type == SONG_END:
            play_a_different_song()


    if gameStatus == "playing":
        handlePlayerinput()
        moveEnemies()
        draw()
        checkCollisions()
        powerUp()
    elif gameStatus == "Gameover":
        drawGameOver()
        resetCount()


    #Show any graphical updates you have made to the screen
    pygame.display.flip()
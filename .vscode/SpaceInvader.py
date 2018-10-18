import pygame

windowWidth = 400
windowHeight = 600
gameSideMargin = 1
gameTopMargin = 30
gameBottomMargin = 25
gameBorderWidth = 3

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Space Invaders')

titleFont = pygame.font.SysFont('Terminal', 40, False)

clock = pygame.time.Clock()

playerImg = pygame.image.load("si-player.gif")
backgroundImg = pygame.image.load("si-background.gif")
enemyImg = pygame.image.load("si-enemy.gif")

class Player:
    xcor = 150
    ycor = windowHeight - gameBottomMargin - gameBorderWidth - playerImg.get_height()
    speed = 5
    direction = 0
    def show(self):
        movementAmount = self.direction * self.speed
        newX = self.xcor + movementAmount

        if newX < gameSideMargin + gameBorderWidth or newX > windowWidth - gameSideMargin - gameBorderWidth - playerImg.get_width():
            self.xcor = self.xcor
        else:
            self.xcor = newX

        gameDisplay.blit(playerImg, (self.xcor, self.ycor))
    def moveRight(self):
        self.direction = 1
    def moveLeft(self):
        self.direction = -1
    def stopMoving(self):
        self.direction = 0

class Enemy:
    xcor = 0
    ycor = 0
    speed = 1
    direction = 1
    def show(self):
        self.xcor += self.direction * self.speed
        gameDisplay.blit(enemyImg, (self.xcor, self.ycor))
    def createEnemies():
        for x in range(0, 5):
            for y in range (0, 3):
                newEnemy = Enemy()
                newEnemy.xcor = gameSideMargin + gameBorderWidth + enemyImg.get_width() * x
                newEnemy.ycor = gameTopMargin + gameBorderWidth + enemyImg.get_height() * y
                newEnemies.append(newEnemy)
        return newEnemies

player = Player()
enemies = Enemy.createEnemies()

isAlive = True
while isAlive:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isAlive = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moveLeft()
            elif event.key == pygame.K_RIGHT:
                player.moveRight()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stopMoving()

    gameDisplay.blit(gameDisplay, (0, 0))
    gameDisplay.fill(black)

    gameWidth = windowWidth - (gameSideMargin * 2) - (gameBorderWidth * 2)
    gameHeight = windowHeight - gameTopMargin - gameBottomMargin - (gameBorderWidth * 2)

    # Draw a white rectangle with the background image just inside of it to create the game border
    pygame.draw.rect(gameDisplay, white, (gameSideMargin, gameTopMargin, windowWidth - gameSideMargin * 2, windowHeight - gameBottomMargin - gameTopMargin))                                 
    gameDisplay.blit(backgroundImg, (gameSideMargin + gameBorderWidth, gameTopMargin + gameBorderWidth), (0, 0, gameWidth, gameHeight))

    player.show()

    titleText = titleFont.render('SPACE INVADERS', False, white)
    gameDisplay.blit(titleText, (windowWidth / 2 - titleText.get_width() / 2, 0))

    clock.tick(60)
    pygame.display.update()
import pygame,random

pygame.init()

WIDTH , HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH , HEIGHT))

clock = pygame.time.Clock()
direction = "UNKNOWN"

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()
        self.surf = pygame.Surface((15,15))
        self.surf.fill((104, 104,104))
        self.rect = self.surf.get_rect()
        self.rect.x = 350
        self.rect.y = 200

    def update(self, keyPressed):
        global direction
       
        if keyPressed[pygame.K_UP] and direction != "DOWN":
            direction = "UP"
        elif keyPressed[pygame.K_DOWN] and direction != "UP":
            direction = "DOWN"
        elif keyPressed[pygame.K_RIGHT] and direction != "LEFT":
            direction = "RIGHT"
        elif keyPressed[pygame.K_LEFT] and direction != "RIGHT":
            direction = "LEFT"



        if direction == "UP":
            self.rect.move_ip(0,-20)
            snakeCoordinates.append((snake.rect.x,snake.rect.y))
        elif direction == "DOWN":
            self.rect.move_ip(0, 20)
            snakeCoordinates.append((snake.rect.x, snake.rect.y))
        elif direction == "RIGHT":
            self.rect.move_ip(20, 0)
            snakeCoordinates.append((snake.rect.x, snake.rect.y))
        elif direction == "LEFT":
            self.rect.move_ip(-20, 0)
            snakeCoordinates.append((snake.rect.x, snake.rect.y))


        ## Border Control
        if self.rect.top < 0:
            self.rect.top = HEIGHT
        if self.rect.top > HEIGHT:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = WIDTH
        if self.rect.left > WIDTH:
            self.rect.left = 0

class Body(pygame.sprite.Sprite):
    def __init__(self):
        super(Body, self).__init__()
        self.surf = pygame.Surface((15,15))
        self.surf.fill((104, 104,104))
        self.rect = self.surf.get_rect()


class Apple(pygame.sprite.Sprite):
    def __init__(self,randomX,randomY):
        super(Apple, self).__init__()
        self.surf = pygame.Surface((15,15))
        self.surf.fill((200,100,50))
        self.rect = self.surf.get_rect()
        self.rect.x = randomX
        self.rect.y = randomY


## Sprite Groups
allSprites = pygame.sprite.Group()
apples = pygame.sprite.Group()
snakes = pygame.sprite.Group()
bodies = pygame.sprite.Group()

snake = Snake()
apple = Apple(100,200)

allSprites.add(apple,snake)
apples.add(apple)
snakes.add(snake)

bodyList = list()
snakeCoordinates = list()

bodyCount = 0

running = True

while running:

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False

    keypressed = pygame.key.get_pressed()

    screen.fill((255,255,255))

    if pygame.sprite.groupcollide(snakes,apples,0,1):
        randomX = random.randint(0, WIDTH)
        randomY = random.randint(0, HEIGHT)
        apple.kill()

        newApple = Apple(randomX, randomY)

        bodyCount += 1
        body = Body()

        allSprites.add(newApple,body)
        apples.add(newApple)
        bodyList.append(body)
        bodies.add(body)

    ## Draw all Sprites
    for sprite in allSprites:
        screen.blit(sprite.surf,sprite.rect)

  
    ## ForLoop for the snake's body to follow its head 
    if len(bodyList) > 0:
        for i in range(len(bodyList)):
            # Her bir parça kendisinden öncekini takip ediyor!
            bodyList[i].rect = snakeCoordinates[-i-2]

            screen.blit(bodyList[i].surf,bodyList[i].rect)

    snakes.update(keypressed)

    pygame.display.flip()

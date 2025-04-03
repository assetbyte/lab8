import pygame,sys,random

pygame.init()

WIDTH,HEIGHT = 600,600
BLOCK_SIZE = 50
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake") 
score = 0
shrift = pygame.font.Font(None, 36) 

clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.x , self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False
        
    def update(self):
        global apple
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0,WIDTH) or self.head.y not in range(0, HEIGHT):
                self.dead = True
        if self.dead:
            self.x , self.y = BLOCK_SIZE, BLOCK_SIZE
            self.xdir = 1
            self.ydir = 0
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.dead = False
            apple = Apple()
            global score 
            score = 0
            
        self.body.append(self.head)
        for i in range(len(self.body)- 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)


class Apple:
    def __init__(self):
        self.x = int(random.randint(0,WIDTH)/BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0,HEIGHT)/BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x , self.y, BLOCK_SIZE, BLOCK_SIZE)
    
    def update(self):
        pygame.draw.rect(screen, "red", self.rect)
    
def drawArea():
    for x in range(0,WIDTH,BLOCK_SIZE):
        for y in range(0,HEIGHT,BLOCK_SIZE):
            rect = pygame.Rect(x,y, BLOCK_SIZE,BLOCK_SIZE)
            pygame.draw.rect(screen, "gray", rect, 1 )

def draw_score():
    text = shrift.render(f"Score: {score}", True, "white")
    screen.blit(text, (10, 10))
drawArea()
snake = Snake()
apple = Apple()
run = True
while run:
    screen.fill("black")
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif ev.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif ev.key == pygame.K_RIGHT:
                snake.ydir = 0 
                snake.xdir = 1 
            elif ev.key == pygame.K_LEFT:
                snake.ydir = 0 
                snake.xdir = -1
    snake.update()
    screen.fill("black")
    drawArea()
    apple.update()
    pygame.draw.rect(screen, "green", snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)
    draw_score()
    
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()
        score += 1 
    pygame.display.update()
    clock.tick(7)
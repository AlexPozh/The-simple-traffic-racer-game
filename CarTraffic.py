import pygame
import random
import time


'''
# CONSTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
colors = [WHITE, BLACK, RED, GREEN, BLUE]
WIDTH = 800  # ширина игрового окна
HEIGHT = 800 # высота игрового окна
FPS = 30 # частота кадров в секунду
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fool")
clock = pygame.time.Clock()
x = 0
y = 800
r = 20
move = ""
Y = 0
X = 0
screen.fill(BLUE)
pygame.display.update()
# Game
playing = True
while playing:
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                move = "Go"
                X = event.pos[0]
                Y = event.pos[1]
    screen.fill(BLUE)
    pygame.draw.circle(screen, WHITE, (X, y), r)
    if y != Y and move == "Go":
        y -= 1
    else:
        pygame.draw.rect(screen, RED, (X-25, Y-25, 50,50))
        x = X
        y = 800
        move = ''
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

''' 


'''
# CONSTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [WHITE, BLACK, RED, GREEN, BLUE]
WIDTH = 800  # ширина игрового окна
HEIGHT = 800 # высота игрового окна
FPS = 30 # частота кадров в секунду


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fool")
clock = pygame.time.Clock()

# Cлой - прямоугольник
xR = 20
yR = 20
surfRect = pygame.Surface((30,20))
surfRect.fill(RED)
# Cлой - квадрат первый 
xS1 = 100
yS1 = 600
surfSq = pygame.Surface((20,20))
surfSq.fill(WHITE)
# Cлой - круг
xC = 390
yC = 590
surfCir = pygame.Surface((50,50))
surfCir.fill(RED)
pygame.draw.circle(surfCir,GREEN,(25,25), 10)
# Cлой - квадрат второй
xS2 = 700
yS2 = 600
surfSq2 = pygame.Surface((20,20))
surfSq2.fill(BLUE)
# Cлой - первая часть экрана
surf_UpSc = pygame.Surface((WIDTH, HEIGHT // 2))
surf_UpSc.fill(BLUE)

surf_UpSc.blit(surfRect, (xR,yR))
screen.blit(surf_UpSc, (0,0))
screen.blit(surfSq, (xS1, yS1))
screen.blit(surfCir, (xC,yC))
screen.blit(surfSq2, (xS2, yS2))
pygame.display.update()
move = ""
# Game
playing = True
while playing:
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                move = "Go"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                move = "Go"
    if move == "Go":
        if xR != 780:
            xR += 10
        else: 
            xR = 20

        if yS1 != 400:
            yS1 -= 10
        else:
            yS1 = 600

        if xC != 490:
            xC += 10
        else:
            xC = 390
        
        if yS2 != 400:
            yS2 -= 10
        else:
            yS2 = 600
    surf_UpSc.fill(BLUE)
    screen.fill(BLACK)
    surf_UpSc.blit(surfRect, (xR,yR))
    screen.blit(surf_UpSc, (0,0))
    screen.blit(surfSq, (xS1, yS1))
    screen.blit(surfCir, (xC,yC))
    screen.blit(surfSq2, (xS2, yS2))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
'''  
"""

# CONSTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [WHITE, BLACK, RED, GREEN, BLUE]
WIDTH = 800  # ширина игрового окна
HEIGHT = 800 # высота игрового окна
FPS = 30 # частота кадров в секунду

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fool")
clock = pygame.time.Clock()

sqr = pygame.Surface((50,100))
sqr.fill(BLUE)
rect = sqr.get_rect(x=200, y = 400)

f = pygame.font.Font(None, 36)
t = f.render("Crash!!", 1, GREEN)

r = pygame.Surface((100,100))
rR = r.get_rect(x=400,y=600)
r.fill(WHITE)
screen.blit(r,rR)
pygame.display.update()
# Game
playing = True
moving = False
while playing:
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == pygame.MOUSEBUTTONUP:
                moving = False
        elif event.type == pygame.MOUSEMOTION and moving:
                rect.move_ip(event.rel)
    screen.fill(BLACK)
    sqr.fill(BLUE)
    screen.blit(sqr,rect)
    # pygame.draw.rect(screen, RED, rect)
    
    if rR.contains(rect):
 
        screen.blit(t, (400,400))
        
        pygame.display.update()
    screen.blit(r,rR)
    pygame.display.update()


    clock.tick(FPS)
pygame.quit()

"""  

'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [WHITE, BLACK, RED, GREEN, BLUE]
WIDTH = 800  # ширина игрового окна
HEIGHT = 800 # высота игрового окна
FPS = 30 # частота кадров в секунду

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fool")
clock = pygame.time.Clock()

car = pygame.image.load("car.png").convert_alpha()
carR = car.get_rect(center = (400, 400))

carUp = car
carDown = pygame.transform.flip(car, False, True)
carLeft = pygame.transform.rotate(car, 90)
carRight = pygame.transform.rotate(car, 270)

screen.blit(car, (carR))
pygame.display.update()
move = ""


posOfCar = car
coordOfCar = carR
def currentPosition():
    screen.blit(posOfCar, coordOfCar)
    pygame.display.update()
# Game
playing = True
while playing:
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move = "Up"
            elif event.key == pygame.K_DOWN:
                move = "Down"
            elif event.key == pygame.K_LEFT:
                move = "Left"
            elif event.key == pygame.K_RIGHT:
                move = "Right"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move = ''
                posOfCar = carUp 
                coordOfCar = carR
            elif event.key == pygame.K_DOWN:
                move = ''
                posOfCar = carDown 
                coordOfCar = carR
               
            elif event.key == pygame.K_LEFT:
                move = ''
                posOfCar = carLeft 
                coordOfCar = carR
            elif event.key == pygame.K_RIGHT:
                move = ''
                posOfCar = carRight 
                coordOfCar = carR
                
    screen.fill(BLACK)
    # currentPosition()
    if move == "Up":
        carR.y -= 10
        screen.blit(carUp, (carR))
    elif move == "Down":
        carR.y += 10
        screen.blit(carDown, (carR))
    elif move == "Left":
        carR.x -= 10
        screen.blit(carLeft, (carR))
    elif move == "Right":
        carR.x += 10
        screen.blit(carRight, (carR))
    else:
        currentPosition()
    pygame.display.update()


    clock.tick(FPS)
pygame.quit()
'''  

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [WHITE, BLACK, RED, GREEN, BLUE]
WIDTH = 800  # ширина игрового окна
HEIGHT = 800 # высота игрового окна
FPS = 30 # частота кадров в секунду

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fool")
clock = pygame.time.Clock()

back = pygame.image.load("background.png").convert_alpha()
backR = back.get_rect()
carsImage = ("car1.png","car2.png","car3.png")
cars_surf = [pygame.image.load(car).convert_alpha() for car in carsImage]
def speedOFCars() -> int:
    # try:
    #     speed = int(input("Please, write a speed, which u want other cars to spawn in the map!:\n"))
    #     return speed
    # except:
    #     print("U didnt write a normal number, so the game will start with a default value of the speed (3 seconds)")
    #     return 3000
    return 1200
spawnCars = pygame.USEREVENT + 0
pygame.time.set_timer(spawnCars, speedOFCars())
stop = ""
class Player(pygame.sprite.Sprite):
    def __init__(self,surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(surf, 180)
        self.rect = self.image.get_rect(center = (400, 700))
        self.speed = 2
        self.move = ""
        self.add(group)
    def update(self):
        if self.move == "Left" and stop != "STOP":
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0

        elif self.move == "Right" and stop != "STOP":
            self.rect.x += self.speed
            if self.rect.topright[0] > 800:
                self.rect.x = 770


class Car(pygame.sprite.Sprite):
    def __init__(self, x, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center = (x, 0))
        self.add(group)
        self.speed = random.randint(1,4)
       
    def update(self):
        if self.rect.y < HEIGHT and stop != "STOP":
            self.rect.y += self.speed
        elif  self.rect.y > HEIGHT:
            self.kill()



t = pygame.font.Font(None, 35)
def timer(currentTime):
    if stop != "STOP":
        timer = t.render(f"Time : {currentTime}", 1, RED)
        screen.blit(timer, (25, 13))
    else:
        textLose = pygame.font.Font(None, 50)
        text = textLose.render("You lose!", 1, RED)
        tR = text.get_rect(center = (400, 400))
        screen.blit(text, tR )

cars = pygame.sprite.Group()
player = pygame.sprite.Group()
Car(random.randint(1,800), random.choice(cars_surf),cars)
p = Player(cars_surf[0], player)
screen.blit(back, backR)



def collision():
    global stop
    for car in cars:
        if p.rect.colliderect(car.rect):
            stop = "STOP"


# Game
playing = True
startGame = time.time()
while playing:
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == spawnCars:
            if stop != "STOP":
                Car(random.randint(1,800), random.choice(cars_surf),cars)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p.move = "Left"
            elif event.key == pygame.K_RIGHT:
                p.move = "Right"
        elif event.type == pygame.KEYUP:
            p.move = ""

    collision()

    screen.blit(back, backR)

    player.draw(screen)

    cars.draw(screen)

    timer(int(time.time() - startGame))

    pygame.display.update()

    clock.tick(FPS)

    cars.update()

    player.update()

pygame.quit()







import pygame
import random
import time

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
    # Events
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

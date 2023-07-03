import pygame
import random
import time

# Consts - Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [WHITE, BLACK, RED, GREEN, BLUE]
WIDTH = 800  # width of the screen
HEIGHT = 800 # heigh of the screen
FPS = 30 # frames per seconds

pygame.init() # start a pygame library
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # create the screen, where there will be our game
pygame.display.set_caption("Car Racer") # the nmae of the game 
clock = pygame.time.Clock() # getting time for our FPS

back = pygame.image.load("background.png").convert_alpha() # backround of the game
backR = back.get_rect()

carsImage = ("car1.png","car2.png","car3.png")
cars_surf = [pygame.image.load(car).convert_alpha() for car in carsImage] # after curs_surf will be the list of the car's surfaces

def appearanceCars() -> int: # the speed of appearance of the cars
    return 1200
    
spawnCars = pygame.USEREVENT + 0 # creating the user's event
pygame.time.set_timer(spawnCars, appearanceCars())
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

cars = pygame.sprite.Group() # creating a group of the car sprites
player = pygame.sprite.Group() # creating a player's group 

Car(random.randint(1,800), random.choice(cars_surf),cars) # creating the instance of the class Car(the first car)
p = Player(cars_surf[0], player) # creating the instance of the class Player

screen.blit(back, backR) # drawinng the background

def collision(): # to define collision of the cars 
    global stop
    for car in cars:
        if p.rect.colliderect(car.rect):
            stop = "STOP" # game lose

# Game
playing = True
startGame = time.time() # the start of the game timer
while playing:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == spawnCars:
            if stop != "STOP":
                Car(random.randint(1,800), random.choice(cars_surf),cars) # appearance a new car
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p.move = "Left"
            elif event.key == pygame.K_RIGHT:
                p.move = "Right"
        elif event.type == pygame.KEYUP:
            p.move = ""

    collision() # updating the function

    screen.blit(back, backR) # drawing the background

    player.draw(screen) # drawing the player

    cars.draw(screen) # drawing the cars

    timer(int(time.time() - startGame)) # updating the function

    pygame.display.update() # updating the screen
 
    clock.tick(FPS) # FPS control

    cars.update() # updating the screen
 
    player.update() # updating the screen

pygame.quit()

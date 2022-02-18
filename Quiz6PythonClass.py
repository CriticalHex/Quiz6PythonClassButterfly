import pygame
from math import pi
pygame.init

#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Butterflyu")
clock = pygame.time.Clock()

#game variables
doExit = False #variable to quit out of game loop

class Butterfly:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(screen, (150,0,200), (self.x + 75 , self.y + 125), 75) #bottom circles
        pygame.draw.circle(screen, (150,0,200), (self.x + -25 , self.y + 125), 75)

        pygame.draw.circle(screen, (150,0,150), (self.x + 75 , self.y + 80), 80) #top circles
        pygame.draw.circle(screen, (150,0,150), (self.x + -25 , self.y + 80), 80)

        pygame.draw.ellipse(screen, (255,255,0), (self.x, self.y, 50,200)) #body

        pygame.draw.arc(screen, (200,0,0), (self.x, self.y + 40, 50, 25), (10*pi)/9, (17*pi)/9, 5) #arcs
        pygame.draw.arc(screen, (200,0,0), (self.x, self.y + 60, 50, 25), (10*pi)/9, (17*pi)/9, 5)
        pygame.draw.arc(screen, (200,0,0), (self.x, self.y + 80, 50, 25), (10*pi)/9, (17*pi)/9, 5)
        pygame.draw.arc(screen, (200,0,0), (self.x, self.y + 100, 50, 25), (10*pi)/9, (17*pi)/9, 5)
        pygame.draw.arc(screen, (200,0,0), (self.x, self.y + 120, 50, 25), (10*pi)/9, (17*pi)/9, 5)

        pygame.draw.line(screen, (0,0,0), (self.x + 20, self.y + 5), (self.x - 50 + 20, self.y - 50 + 5), 5) #antenna
        pygame.draw.line(screen, (0,0,0), (self.x + 30, self.y + 5), (self.x + 50 + 30, self.y - 50 + 5), 5)


b1 = Butterfly(375,300)
b2 = Butterfly(100,0)
b3 = Butterfly(650,600)
b4 = Butterfly(650,0)
b5 = Butterfly(100,600)

#BEGIN GAME LOOP######################################################
while not doExit:
   
    clock.tick(60) #FPS (frames per second)
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
  
     
    #render section-----------------------------------
 
    screen.fill((0,0,125))

    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()

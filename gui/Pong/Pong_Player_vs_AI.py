import pygame
from pygame.locals import *

pointcounter = 0

class Pong(object):
    def __init__(self, screensize):
        #Set Screensize
        self.screensize = screensize

        #Sets Center of Screen
        self.centerx = int(screensize[0] * 0.5)
        self.centery = int(screensize[1] * 0.5)

        #Sets Radius of Ball
        self.radius = 8

        #Creates Ball
        self.rect = pygame.Rect((self.centerx - self.radius), (self.centery - self.radius), (self.radius * 2), (self.radius * 2))

        #Sets Color
        self.color = (255, 255, 255)

        #Sets Direction
        self.direction = [1, 1]

        #Speed of Ball
        self.speedx = 5
        self.speedy = 5

        #Edge Booleans
        self.hit_edge_left = False
        self.hit_edge_right = False

    def update(self, player_paddle, ai_paddle):

        global pointcounter

        #Sets Center Variables
        self.centerx += self.direction[0] * self.speedx
        self.centery += self.direction[1] * self.speedy

        #Centers Rectangle
        self.rect.center = (self.centerx, self.centery)

        #Checks
        if self.rect.top <= 0:
            self.direction[1] = 1
        elif self.rect.bottom >= self.screensize[1] - 1:
            self.direction[1] = -1

        #Checks for Edges
        if self.rect.right >= self.screensize[0] - 1:
            self.hit_edge_right = True
        elif self.rect.left <= 0:
            self.hit_edge_left = True

        #Checks for Paddle Collision
        if self.rect.colliderect(player_paddle.rect):
            self.direction[0] = -1
            pointcounter += 1
        if self.rect.colliderect(ai_paddle.rect):
            self.direction[0] = 1

    #Renders Game
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (0, 0, 0), self.rect.center, self.radius, 1)

#Creates the AI Paddle
class AIPaddle(object):
    def __init__(self, screensize):
        #Sets Screensize
        self.screensize = screensize

        #Sets Center
        self.centerx = 5
        self.centery = int(screensize[1] * 0.5)

        #AI Paddle Dimensions
        self.height = 100
        self.width = 10

        #Defines AI Paddle
        self.rect = pygame.Rect(0, self.centery - int(self.height * 0.5), self.width, self.height)

        #Sets Color
        self.color = (255, 255, 255)
        
        #AI Paddle Speed
        self.speed = 6

    def update(self, pong):
        #Updates AI Paddle Center Based on Ball
        if pong.rect.top < self.rect.top:
            self.centery -= self.speed
        elif pong.rect.bottom > self.rect.bottom:
            self.centery += self.speed

        #Sets AI Paddle Center
        self.rect.center = (self.centerx, self.centery)

    #Renders AI Paddle
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)

#Creates Player Paddle
class PlayerPaddle(object):
    def __init__(self, screensize):
        #Sets Screensize
        self.screensize = screensize

        #Sets Center of Player Paddle
        self.centerx = screensize[0] - 5
        self.centery = int(screensize[1] * 0.5)

        #Player Paddle Dimensions
        self.height = 100
        self.width = 10

        #Creates Player Paddle
        self.rect = pygame.Rect(0, (self.centery - int(self.height * 0.5)), self.width, self.height)

        self.color = (255, 255, 255)

        #Player Paddle Speed
        self.speed = 10
        self.direction = 0

    def update(self):
        #Sets Center
        self.centery += self.direction * self.speed

        #Sets Center of Player Paddle
        self.rect.center = (self.centerx, self.centery)

        #Constrains Player Paddle
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screensize[1] - 1:
            self.rect.bottom = self.screensize[1] - 1

    #Render Player Paddle
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)


def main():
    #Initialize Pygame
    pygame.init()

    global pointcounter

    #Screensize Initailized
    screensize = (1600, 800)

    #Creates Screen
    screen = pygame.display.set_mode(screensize, pygame.FULLSCREEN)

    #Creates Clock
    clock = pygame.time.Clock()

    #Initializes Classes
    pong = Pong(screensize)
    ai_paddle = AIPaddle(screensize)
    player_paddle = PlayerPaddle(screensize)

    #Main Boolean
    running = True

    #Game Loop
    while running:

        #Sets Clock Tick Rate
        clock.tick(64)

        #Checks Keys
        for event in pygame.event.get():
            #Checks for Esc Key
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            #Player Paddle Control while Pressed
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player_paddle.direction = -1
                elif event.key == K_DOWN:
                    player_paddle.direction = 1

            #Player Paddle Control while not Pressed
            if event.type == KEYUP:
                if event.key == K_UP and player_paddle.direction == -1:
                    player_paddle.direction = 0
                elif event.key == K_DOWN and player_paddle.direction == 1:
                    player_paddle.direction = 0

        #Update Paddles
        ai_paddle.update(pong)
        player_paddle.update()
        pong.update(player_paddle, ai_paddle)

        #Checks for Win Case
        if pong.hit_edge_left:
            print ('You Won')
            running = False
            
        elif pong.hit_edge_right:
            print ('Your Score')
            print (pointcounter)
            running = False

        #Redraw Screen
        screen.fill((0,0,0))

        #Renders Paddles in Screen
        ai_paddle.render(screen)
        player_paddle.render(screen)
        pong.render(screen)

        #Update Display
        pygame.display.flip()
        
    #Shutsdown Pygame
    pygame.quit()

#Runs Main Method
main()

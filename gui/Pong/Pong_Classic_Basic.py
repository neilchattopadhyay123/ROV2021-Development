import pygame
import random
import sys

class Paddle(pygame.Rect):
    def __init__(self, velocity, up_key, down_key, *args, **kwargs):
        #Velocity
        self.velocity = velocity
        #Contol Kys
        self.up_key = up_key
        self.down_key = down_key

        #Super Fuction
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_height):
        #Grabs Key
        keys_pressed = pygame.key.get_pressed()

        #Checks Key and Moves Paddle
        if keys_pressed[self.up_key]:
            if self.y - self.velocity > 0:
                self.y -= self.velocity

        #Checks Key and Moves Paddle
        if keys_pressed[self.down_key]:
            if self.y + self.velocity < board_height - self.height:
                self.y += self.velocity


class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        #Velocity X-Axis
        self.velocity = velocity
        #Velocity Y-Axis
        self.angle = 0
        
        #Super Function
        super().__init__(*args, **kwargs)

    def move_ball(self):
        self.x += self.velocity
        self.y += self.angle

class Pong:
    #Screen Dimensions
    SCREEN_HEIGHT = 800
    SCREEN_WIDTH = 1600

    #Paddle Dimensions
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100
    
    #Ball Dimensions
    BALL_WIDTH = 10
    BALL_VELOCITY = 10

    WHITE = (255, 255, 255)

    RUNNING = True

    def __init__(self):
        #Initialize Pygame
        pygame.init()

        #Create Screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        #Resets Values of Screen
        SCREEN_HEIGHT = pygame.display.Info().current_h
        SCREEN_WIDTH = pygame.display.Info().current_w

        #Create the player objects.
        self.paddles = []
        self.balls = []

        #Left Paddle
        self.paddles.append(Paddle(self.BALL_VELOCITY, pygame.K_w, pygame.K_s, 0,
            self.SCREEN_HEIGHT / 2 - self.PADDLE_HEIGHT / 2,self.PADDLE_WIDTH,self.PADDLE_HEIGHT))

        #Right Paddle
        self.paddles.append(Paddle(self.BALL_VELOCITY, pygame.K_UP, pygame.K_DOWN, self.SCREEN_WIDTH - self.PADDLE_WIDTH,
            self.SCREEN_HEIGHT / 2 - self.PADDLE_HEIGHT / 2, self.PADDLE_WIDTH, self.PADDLE_HEIGHT))

        #Ball
        self.balls.append(Ball(self.BALL_VELOCITY, self.SCREEN_WIDTH / 2 - self.BALL_WIDTH / 2,
            self.SCREEN_HEIGHT / 2 - self.BALL_WIDTH / 2, self.BALL_WIDTH, self.BALL_WIDTH))


    def check_for_wall(self):
        for ball in self.balls:
            #Game Ends if Ball Hits Left or Right Edge
            if ball.x > self.SCREEN_WIDTH or ball.x < 0:
                self.RUNNING = False
            #Changes Ball Direction if hits top or bottom edge of screen
            if ball.y > self.SCREEN_HEIGHT - self.BALL_WIDTH or ball.y < 0:
                ball.angle = -ball.angle

    def check_for_paddle(self):
        for ball in self.balls:
            for paddle in self.paddles:
                #Checks if Ball and Paddle Overlap
                if ball.colliderect(paddle):
                    ball.velocity = -ball.velocity
                    ball.angle = random.randint(-10, 10)
                    break
                
    def game_loop(self):
        while self.RUNNING:
            #Checks for Esc Key
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.RUNNING = False
                    break

            #Redraw screen
            self.screen.fill((0, 0, 0))

            #Checks ball location and walls
            self.check_for_wall()
            self.check_for_paddle()

            #Paddle Drawing/Movement
            for paddle in self.paddles:
                paddle.move_paddle(self.SCREEN_HEIGHT)
                pygame.draw.rect(self.screen, self.WHITE, paddle)

            #Ball Drawing/Movement
            for ball in self.balls:
                ball.move_ball()
                pygame.draw.rect(self.screen, self.WHITE, ball)

            #Update Pygame Display
            pygame.display.flip()
            self.clock.tick(60)

if __name__=='__main__':
    pong = Pong()
    pong.game_loop()
    pygame.quit()

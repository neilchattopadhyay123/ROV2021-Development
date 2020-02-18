import pygame
import random
import sys

class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        #Velocity X-Axis
        self.velocity = velocity
        self.vel_mod = 1
        #Velocity Y-Axis
        self.angle = 0
        
        #Super Function
        super().__init__(*args, **kwargs)

    def move_ball(self):
        #Ball Speed Cap
        if self.vel_mod > 2:
            self.vel_mod = 2
            
        self.x += self.velocity * self.vel_mod
        self.y += self.angle
        
    def reset_ball(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord

        
class Paddle(pygame.Rect):
    
    def __init__(self, velocity, up_key, down_key, *args, **kwargs):
        #Velocity
        self.velocity = velocity
        #Contol Kys
        self.up_key = up_key
        self.down_key = down_key

        #Super Fuction
        super().__init__(*args, **kwargs)

    def reset_paddle(self, board_height):
        self.y = board_height/2

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

    def move_paddle_AI(self, board_height, ball_y_cord, ball_x_cord, paddle_height, screen_width, random_error):
        #Random Error Generation
        offset = paddle_height
        if random_error == 1:
            #Sets Center of Paddle
            center_y = self.y + (paddle_height / 2)

            #Checks Where Ball is in Relation to Paddle with Offset
            if center_y > ball_y_cord + offset:
                self.y -= self.velocity
            elif center_y < ball_y_cord - offset:
                self.y += self.velocity
                
        else:
            #Sets Center of Paddle
            center_y = self.y + (paddle_height / 2)

            #Checks Where Ball is in Relation to Paddle
            if center_y > ball_y_cord:
                self.y -= self.velocity
            elif center_y < ball_y_cord:
                self.y += self.velocity

        #Constrains Paddle
        if self.y < 0:
            self.y = 0
        elif self.y + paddle_height > board_height:
            self.y = board_height - paddle_height
        
    
class Pong:
    #Screen Dimensions
    SCREEN_HEIGHT = 800
    SCREEN_WIDTH = 1600
    
    #Ball Dimensions
    BALL_WIDTH = 10
    BALL_VELOCITY = 5
    BALL_Y_CORD = 0
    BALL_X_CORD = 0

    #Paddle Dimensions
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100
    PADDLE_VELOCITY = 5
    
    #Sets Color of All Atributes
    COLOR = (255, 255, 255)

    #Main Booleans
    RUNNING = True
    MANUALCONTROL = True

    #Points
    RIGHTPOINTS = 0
    LEFTPOINTS = 0

    #Left Paddle Controls
    LEFT_UP_KEY = pygame.K_w
    LEFT_DOWN_KEY = pygame.K_s

    #Right Paddle Controls
    RIGHT_UP_KEY = pygame.K_UP
    RIGHT_DOWN_KEY = pygame.K_DOWN

    #Backgroud
    BACKGROUND = pygame.image.load("resources/Black_Wallpaper.jpg")

    '''
    Wallpapers
    1. Wallpaper.jpg
    2. White_Wallpaper.jfif
    3. Black_Wallpaper.jpg
    '''

    #Fonts
    FONT_SIZE = 75
    FONT_TYPE = 'freesansbold.ttf'

    #Centerline
    CENTERLINE_WIDTH = 2

    #Random Error
    RANDOM_ERROR = 0
    RANDOM_ERROR_PROBABILITY = 4
    
    def __init__(self):
        #Initialize Pygame
        pygame.init()
        pygame.font.init() 

        #Create Screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        #Set Background Image
        BACKGROUND = pygame.transform.scale(self.BACKGROUND,(pygame.display.Info().current_w, pygame.display.Info().current_h))
        self.screen.blit(BACKGROUND, [0, 0])
        
        #Resets Values of Screen
        SCREEN_HEIGHT = pygame.display.Info().current_h
        SCREEN_WIDTH = pygame.display.Info().current_w

        #Create the player objects.
        self.paddles = []
        self.balls = []


        #Left Paddle
        self.paddles.append(Paddle(self.PADDLE_VELOCITY, self.LEFT_UP_KEY, self.LEFT_DOWN_KEY, 0,
            self.SCREEN_HEIGHT / 2 - self.PADDLE_HEIGHT / 2,self.PADDLE_WIDTH,self.PADDLE_HEIGHT))

        #Right Paddle
        self.paddles.append(Paddle(self.PADDLE_VELOCITY, self.RIGHT_UP_KEY, self.RIGHT_DOWN_KEY, self.SCREEN_WIDTH - self.PADDLE_WIDTH,
            self.SCREEN_HEIGHT / 2 - self.PADDLE_HEIGHT / 2, self.PADDLE_WIDTH, self.PADDLE_HEIGHT))

        #Ball
        self.balls.append(Ball(self.BALL_VELOCITY, self.SCREEN_WIDTH / 2 - self.BALL_WIDTH / 2,
            self.SCREEN_HEIGHT / 2 - self.BALL_WIDTH / 2, self.BALL_WIDTH, self.BALL_WIDTH))


    def check_for_wall(self):
        for ball in self.balls:
            #Changes Ball Direction if hits top or bottom edge of screen
            if ball.y > self.SCREEN_HEIGHT - self.BALL_WIDTH or ball.y < 0:
                ball.angle = -ball.angle
                
            #Ball Hits Right Add Point
            if ball.x < 0:
                self.RIGHTPOINTS = self.RIGHTPOINTS + 1
                ball.reset_ball(self.SCREEN_WIDTH / 2 - self.BALL_WIDTH / 2, self.SCREEN_HEIGHT / 2 - self.BALL_WIDTH / 2)
                print("Right = " + str(self.RIGHTPOINTS))
                ball.vel_mod = 1
                self.RANDOM_ERROR = 0
                
            #Ball Hits Left Edge Add Point
            if ball.x > self.SCREEN_WIDTH:
                self.LEFTPOINTS = self.LEFTPOINTS + 1
                ball.reset_ball(self.SCREEN_WIDTH / 2 - self.BALL_WIDTH / 2, self.SCREEN_HEIGHT / 2 - self.BALL_WIDTH / 2)
                print("Left = " + str(self.LEFTPOINTS))
                ball.vel_mod = 1
                self.RANDOM_ERROR = 0


    def update_text(self):
        #Creates Lefttext
        LEFTTEXT = pygame.font.Font(self.FONT_TYPE, self.FONT_SIZE)
        LEFTTEXTDISPLAY = LEFTTEXT.render(str(self.LEFTPOINTS), False, self.COLOR)

        #Create Rightext
        RIGHTTEXT = pygame.font.Font(self.FONT_TYPE, self.FONT_SIZE)
        RIGHTTEXTDISPLAY = RIGHTTEXT.render(str(self.RIGHTPOINTS), False, self.COLOR)

        #Reders Text
        self.screen.blit(LEFTTEXTDISPLAY,(self.SCREEN_WIDTH/2 - self.FONT_SIZE,0))
        self.screen.blit(RIGHTTEXTDISPLAY,(self.SCREEN_WIDTH/2 + self.FONT_SIZE/2, 0))



    def check_for_paddle(self):
        for ball in self.balls:
            for paddle in self.paddles:
                #Checks if Ball and Paddle Overlap
                if ball.colliderect(paddle):
                    self.RANDOM_ERROR = random.randint(0,(self.RANDOM_ERROR_PROBABILITY - 1))
                    ball.velocity = -ball.velocity
                    ball.vel_mod += 0.1
                    ball.angle = random.randint(-10, 10)
                    break
                
    def game_loop(self):
        while self.RUNNING:
            #Checks for Keys
            for event in pygame.event.get():
                #Checks for Esc key to exit game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.RUNNING = False
                    break
                #Checks for '1' key to activate AI
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    self.MANUALCONTROL = not(self.MANUALCONTROL)
                    for paddle in self.paddles:
                        paddle.reset_paddle(self.SCREEN_HEIGHT)

            #Redraw entire screen
            self.screen.blit((pygame.transform.scale(self.BACKGROUND,(pygame.display.Info().current_w, pygame.display.Info().current_h))), (0, 0))
            self.update_text()
            pygame.draw.rect(self.screen, self.COLOR, (self.SCREEN_WIDTH/2, 0, self.CENTERLINE_WIDTH, self.SCREEN_HEIGHT))

            #Grabs Ball Coordinates
            for ball in self.balls:
                self.BALL_Y_CORD = ball.y
                self.BALL_X_CORD = ball.x
            
            #Checks ball location and walls
            self.check_for_wall()
            self.check_for_paddle()

            #Paddle Drawing/Movement
            if(self.MANUALCONTROL):
                for paddle in self.paddles:
                    paddle.move_paddle(self.SCREEN_HEIGHT)
                    pygame.draw.rect(self.screen, self.COLOR, paddle)
            else:
                for paddle in self.paddles:
                    #Left Paddle Movement
                    if self.BALL_X_CORD <= self.SCREEN_WIDTH/2:
                        self.paddles[0].move_paddle_AI(self.SCREEN_HEIGHT, self.BALL_Y_CORD, self.BALL_X_CORD, self.PADDLE_HEIGHT, self.SCREEN_WIDTH, self.RANDOM_ERROR)
                        pygame.draw.rect(self.screen, self.COLOR, paddle)

                    #Right Paddle Movement
                    if self.SCREEN_WIDTH/2 < self.BALL_X_CORD and self.BALL_X_CORD <= self.SCREEN_WIDTH:
                        self.paddles[1].move_paddle_AI(self.SCREEN_HEIGHT, self.BALL_Y_CORD, self.BALL_X_CORD, self.PADDLE_HEIGHT, self.SCREEN_WIDTH, self.RANDOM_ERROR)
                        pygame.draw.rect(self.screen, self.COLOR, paddle)

            #Ball Drawing/Movement
            for ball in self.balls:
                ball.move_ball()
                pygame.draw.rect(self.screen, self.COLOR, ball)

            #Update Pygame Display
            pygame.display.flip()
            self.clock.tick(60)

if __name__=='__main__':
    pong = Pong()
    pong.game_loop()
    pygame.quit()

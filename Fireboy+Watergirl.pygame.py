import pygame 
from pygame.locals import *

class Player1:
    def __init__(self, x, y):
        # Load and resize and posistioning the icecube
        self.image = pygame.transform.scale(pygame.image.load('./iceCube_part2_player1.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x =- 0 #left 
        #self.rect.x = screen_width - self.rect.width  #  right  of the screen
        self.rect.y = screen_height - self.rect.height  #  bottom of the screen
        #self.rect.y = 0 #up
        self.velocityY = 0  #for when the ice cube jumps
        self.onGround = True 

   #key movements for x and y coordinates     
    def move_right1(self):
        self.rect.x += 3 # the icecube will move 3 pixels right . forward = + backward = - 
             
    def move_left1(self):
        self.rect.x -= 3 
        
    def move_down1(self):
        self.rect.y  #so the game doesnt end when someone presses the down key 
    
    def jump1(self):
       #if the icecube is on the ground then the icecubec
       while self.onGround:
            self.velocityY = -10  # up = -
            self.onGround = False
            
    def update1(self):
        self.velocityY += 0.5 #amount the icecube can jump (how weak is the gravity)
        self.rect.y += self.velocityY #move the icecube
         # Check if player is on the ground
        if self.rect.y >= screen_height - self.rect.height: #if the y corrdinates of the character is higher than its y height then its jumping  
            self.rect.y = screen_height - self.rect.height #if the icecubes positions height = y coordinate then not jumping 
            self.onGround = True #means the icecube can jump multiple times.
            self.velocityY= 0

    def draw1(self, surface):
        surface.blit(self.image, self.rect) #show on screen(surface)
        
class Player2:
    def __init__(self, x, y):
        # Load and resize and posistioning the icecube
        self.image = pygame.transform.scale(pygame.image.load('./fire.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x =- 0 #left 
        #self.rect.x = screen_width - self.rect.width  #  right  of the screen
        self.rect.y = screen_height - self.rect.height  #  bottom of the screen
        #self.rect.y = 0 #up
        self.velocityY = 0  #for when the ice cube jumps
        self.onGround = True 

   #key movements for x and y coordinates     
    def move_right2(self):
        self.rect.x += 3 # the icecube will move 3 pixels right . forward = + backward = - 
             
    def move_left2(self):
        self.rect.x -= 3 
        
    def move_down2(self):
        self.rect.y  #so the game doesnt end when someone presses the down key 
    
    def jump2(self):
       #if the icecube is on the ground then the icecubec
       while self.onGround:
            self.velocityY = -10  # up = -
            self.onGround = False
            
    def update2(self):
        self.velocityY += 0.5 #amount the icecube can jump (how weak is the gravity)
        self.rect.y += self.velocityY #move the icecube
         # Check if player is on the ground
        if self.rect.y >= screen_height - self.rect.height: #if the y corrdinates of the character is higher than its y height then its jumping  
            self.rect.y = screen_height - self.rect.height #if the icecubes positions height = y coordinate then not jumping 
            self.onGround = True #means the icecube can jump multiple times.
            self.velocityY= 0

    def draw2(self, surface):
        surface.blit(self.image, self.rect) #show on screen(surface)


pygame.init()   
screen_width = 1000
screen_height = 650

screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption('Platformer')

bg_img = pygame.image.load('./jungleBackground.png')
player1 = Player1(10,10)
player2 = Player2(10,10)

run = True
while run:  # code of game keeps looping
    screen.blit(bg_img, (0, 0))  # shows background image onto the screen
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # closes the game
            run = False
            
    userInput1 = pygame.key.get_pressed()
    if userInput1[pygame.K_LEFT]:
        player1.move_left1()
    if userInput1[pygame.K_RIGHT]:
        player1.move_right1()
    if userInput1[pygame.K_DOWN]:
        player1.move_down1()
    if userInput1[pygame.K_UP]:
        player1.jump1()
        
    userInput2 = pygame.key.get_pressed()
    if userInput2[pygame.K_a]:
        player2.move_left2()
    if userInput2[pygame.K_d]:
        player2.move_right2()
    if userInput2[pygame.K_s]:
        player2.move_down2()
    if userInput2[pygame.K_SPACE]:
        player2.jump2()
        
    player1.update1()
    player1.draw1(screen) 
    player2.update2()
    player2.draw2(screen) # Draw the characte
    pygame.display.flip()  # update the display

pygame.quit()





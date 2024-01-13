import pygame 
from pygame.locals import *

tile_size = 50

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
        if self.rect.right < max_x: #boundry 
            self.rect.x += 3  # the icecube will move 3 pixels right . forward = + backward = - 
             
    def move_left1(self):
        if self.rect.left > min_x:
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
        if self.rect.x > 1000:
            self.rect.x = 1000
        else:
            self.rect.x < 0
            self.rect.x = 0


   #key movements for x and y coordinates     
    def move_right2(self):
       if self.rect.right < max_x:
           self.rect.x += 3  # the icecube will move 3 pixels right . forward = + backward = - 
             
    def move_left2(self):
        if self.rect.left > min_x:
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


class Lands():
   def __init__(self,data):
        self.tile_list = []    #empty list    

        rock_img = pygame.image.load('./rocks.png')
        lava_img = pygame.image.load('./lava.png')
        water_img = pygame.image.load('./water.png')
        grass_img = pygame.image.load('./grass.png')


        row_count = 0  #row and collum count for steps = 0 
        for row in data: #looking at the environment_data per row and then within a row per tile 
            collum_count = 0
            for tile in row:
                if tile == 1: #if the tile = 1 meaning there is a step then the step image is scaled to the tile size 
                    img = pygame.transform.scale(rock_img, (tile_size, tile_size)) #would be 50 by 50 
                    scaled_image = img.get_rect() #turned a scaled image into a rectangle an stored in scaled image varable 
                    scaled_image.x = collum_count * tile_size #collum count and tile size = the x cordinate of tiles top left corner 
                    scaled_image.y = row_count * tile_size 
                    tile = (img, scaled_image)  # tile = the info of img and scaled_image
                    self.tile_list.append(tile) # this is then added to the empty list 
                if tile == 2:  
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))  
                    scaled_image = img.get_rect()  
                    scaled_image.x = collum_count * tile_size
                    scaled_image.y = row_count * tile_size 
                    tile = (img, scaled_image)  
                    self.tile_list.append(tile) 
                if tile == 3: 
                    img = pygame.transform.scale(lava_img, (tile_size, tile_size)) 
                    scaled_image = img.get_rect()
                    scaled_image.x = collum_count * tile_size 
                    scaled_image.y = row_count * tile_size 
                    tile = (img, scaled_image)  
                    self.tile_list.append(tile)
                if tile == 4: 
                    img = pygame.transform.scale(water_img, (tile_size, tile_size)) 
                    scaled_image = img.get_rect()  
                    scaled_image.x = collum_count * tile_size 
                    scaled_image.y = row_count * tile_size 
                    tile = (img, scaled_image)  
                    self.tile_list.append(tile) 
                collum_count += 1
            row_count += 1
   def draw(self, screen):
       for tile in self.tile_list:
        screen.blit(tile[0], tile[1])

        
environment_data = [
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 3, 4, 2, 2, 0, 0, 0, 2], 
[2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 2, 2], 
[2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 3, 3, 4, 4, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2], 
[2, 2, 2, 2, 3, 3, 2, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2], 
[2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 4, 4, 0, 2, 0, 0, 0, 0, 0, 2], 
[2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 4, 4, 2, 0, 0, 0, 0, 0, 0, 2], 
[2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2], 
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 0, 0, 0, 2], 
[2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 2], 
]

world = Lands(environment_data)


pygame.init()   
screen_width = 1000
screen_height = 650
min_x = tile_size # Left boundary
min_y = tile_size  # Top boundary
max_x = screen_width - tile_size  # Right boundary
max_y = screen_height  

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

    world.draw(screen)     
    player1.update1()
    player1.draw1(screen) 
    player2.update2()
    player2.draw2(screen) # Draw the characte
    pygame.display.flip()  # update the display
    

pygame.quit()





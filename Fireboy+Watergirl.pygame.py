# RESOURCES USED:
# https://www.geeksforgeeks.org/pygame-tutorial/?ref=lbp with the introduction to pygame 
# https://www.youtube.com/watch?v=W_JRd3ntyBg&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=2 creating the players 
# https://www.youtube.com/watch?v=W_JRd3ntyBg&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=2 creating the environment_data (tiles for lands)
# https://www.youtube.com/watch?v=1_H7InPMjaY 
# https://www.w3schools.com/python/python_inheritance.asp for the inheritance 
# https://www.youtube.com/watch?v=vz8YnvnAPp4 intro screen 
# https://www.youtube.com/watch?v=qbkj81_BOes adding dimonds 
# https://www.youtube.com/watch?v=1_H7InPMjaY&t=677s collision detection for moving rocks 
# https://www.youtube.com/watch?v=1_H7InPMjaY&t=677s collison on static and moving objects (the rocks)
# chatGPT for parts of the collisions, intro and gameover screen (noted in the code)
# https://www.youtube.com/watch?v=G8VsEbVS3F8&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=6 game over if players touch either water or lava 
# https://www.youtube.com/watch?v=yRkyrOWmSl4 game over screen 

import pygame 
from pygame.locals import *
import sys

tile_size = 50
#attempt to create an intro page, doesnt display for very long 
#asked chatGPT for help but the screen still couldnt be displayed 
def intro_page(screen):
    intro = True 
    font = pygame.font.Font(None, 50)
    intro_image = pygame.image.load('./intro_page.png')
    text1 = font.render("Fireboy and Watergirl" ,True, (0, 0, 0))
    text2 = font.render("Press the space to start",True, (0, 0, 0))

    while intro:
         screen.blit(intro_image,(0,0)) 
         screen.blit(text2,(100,100))
         screen.blit(text1,(200,200))
         for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
    
    pygame.display.update()

class Player:
    def __init__(self, x, y, both_images):
        self.image = pygame.transform.scale(pygame.image.load(both_images),(40,40)) #self.image applys to both images, both_images 
        self.rect = self.image.get_rect(x=x, y=y) #the coordinates of the two images 
        self.rect.x =- 0 #left 
        #self.rect.x = screen_width - self.rect.width  #  right  of the screen
        self.rect.y = screen_height - self.rect.height  #  bottom of the screen
        #self.rect.y = 0 #up
        self.velocityY = 0  #for when the fire jumps
        self.onGround = True 
        #boundaries 
        if self.rect.x > 1000: #character cant move more that 1000 spaces left and right 
            self.rect.x = 1000 #will stop at 1000
        else:
            self.rect.x < 0 #cant be less and 0 
            self.rect.x = 0
        self.velocityY = 0  #both images start on the ground 
        self.onGround = True 

    def move_right(self):
        if self.rect.right < max_x: #boundry 
            self.rect.x += 3  # the icecube will move 3 pixels right . forward = + backward = - 
        collision_tile = world.collision_detection(self.rect) #world is an instance of land class. this line of code looks at where the players position is and if it next to a tile 
        if collision_tile:  # Collision detected
            self.rect.right = collision_tile.left # character can onlt go left 
             
    def move_left(self):
        if self.rect.left > min_x:
            self.rect.x -= 3 
        collision_tile = world.collision_detection(self.rect)
        if collision_tile:  # Collision detected
            self.rect.left = collision_tile.right
        
    def move_down(self):
         self.rect.y  #so the game doesnt end when someone presses the down key 
    
    def jump(self):
       #if the icecube is on the ground then the icecubec
       while self.onGround:
            self.velocityY = -12  # up = -
            self.onGround = False
                    
    def update(self, world):
        self.velocityY += 0.5 #amount the icecube can jump (how weak is the gravity)
        self.rect.y += self.velocityY #move the icecube
         # Check if player is on the ground
        if self.rect.y >= screen_height - self.rect.height - 50: #if the y corrdinates of the character is higher than its y height then its jumping  
            self.rect.y = screen_height - self.rect.height - 50 #if the icecubes positions height = y coordinate then not jumping 
            self.onGround = True #means the icecube can jump multiple times.
            self.velocityY= 0

        collision_tile = world.collision_detection(self.rect)
        if collision_tile is not None:
            if self.velocityY > 0:  # Falling down
                self.rect.bottom = collision_tile.top #character can not move down 
                self.onGround = True
                self.velocityY = 0
            elif self.velocityY < 0:  # Moving up
                self.rect.top = collision_tile.bottom #character can not move down 
                self.velocityY = 0 #stops any up and down movement 

    def draw(self, surface):
        surface.blit(self.image, self.rect) #show on screen(surface)


class Player_IceCube(Player): #inheritance 
    def __init__ (self, x, y):
        super().__init__( x, y,'./iceCube_part2_player1.png') 
    # iceCube_part2_player1.png is passed into the Player class using the both_images perameter 
        #add lava 
        
class Player_Fire(Player): #inheritance 
    def __init__ (self, x, y):
        super().__init__( x, y,'./fire.png') 
            

class Lands:
   def __init__(self, data):
        self.tile_list = []    #empty list    

        rock_img = pygame.image.load('./rocks.png')
        water_img = pygame.image.load('./water.png')
        grass_img = pygame.image.load('./grass.png')
        lava_img = pygame.image.load('./lava.png')

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
                    img = pygame.transform.scale(grass_img, (tile_size, 40))  
                    scaled_image = img.get_rect()  
                    scaled_image.x = collum_count * tile_size
                    scaled_image.y = row_count * tile_size 
                    tile = (img, scaled_image)  
                    self.tile_list.append(tile) 
                if tile == 3: 
                    lava = Lava(collum_count * tile_size, row_count * tile_size)
                    lava_group.add(lava)
                if tile == 4: 
                    water = Water(collum_count * tile_size, row_count * tile_size)
                    water_group.add(water)
                collum_count += 1
            row_count += 1

   def draw(self, screen):
       for tile in self.tile_list:
        screen.blit(tile[0], tile[1])
#attempt 1 for colision detection 
   #def colision_detection(self,tile, player1,player2):
       #collision_tolerance = 0 
       # if player1.colliderect(tile):
            #if abs(tile.top - player1.bottom) < collision_tolerance:
             #  player1.y -= 0.5
            #if abs(tile.bottom - player1.top) < collision_tolerance:
             #   player1.y += -0.5
            #if abs(tile.right - player1.left) < collision_tolerance:
               # player1 += 0.5
#attempt 2 for colision detection 
   #def colision_detection(self, player2, player1):
       #for tile in self.tile_list:
         #  if player1.colliderect(tile[1]):
            #   return True 
          # if player2.colliderect(tile[1]):
              # return True 
       #return False
#attempt 3 = had to ask chatGPT for help on how to do collision detection 
   def collision_detection(self, player_rect):
        for tile in self.tile_list:
            if player_rect.colliderect(tile[1]):
                return tile[1]   
              
class Water(pygame.sprite.Sprite):
     def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame. image. load ('./water.png')
        self.image = pygame.transform.scale(img, (tile_size, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Lava(pygame.sprite.Sprite):
     def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame. image. load ('./lava.png')
        self.image = pygame.transform.scale(img, (tile_size, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


environment_data = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0], 
[0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 3, 3, 4, 4, 0, 2, 2, 2, 2, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 2, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0], 
[0, 4, 2, 2, 0, 0, 0, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 0, 0], 
[2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 3, 3, 2, 2, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 4, 2, 3], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
]

lava_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
world = Lands(environment_data)

pygame.init()

game_over = False 
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 650
min_x = 0 # Left boundary
min_y = tile_size  # Top boundary
max_x = screen_width   # Right boundary
max_y = screen_height  

#displaying the screen called platformer 
screen = pygame.display.set_mode((screen_width, screen_height)) 
intro_page(screen)  
pygame.display.set_caption('Platformer')
bg_img = pygame.image.load('./jungleBackground.png')

player1 = Player_IceCube(10,10)
player2 = Player_Fire(10,10)

#----------------------------------------------------
#MOVING ROCKS
#moving platforms for two rock images 
platform_velocity= 3 #speed 
platform_velocity2= 3

#rock one, loading, scaling and positioning 
moving_rock_img = pygame.image.load('./rocks.png')
moving_rock_img = pygame.transform.scale(moving_rock_img, (tile_size, 25))
Mrock_rect = moving_rock_img.get_rect(x=100, y=100) #positioning of rock 

#rock two loading, scaling and positioning 
moving_rock2_img = pygame.image.load('./rocks.png')
moving_rock2_img = pygame.transform.scale(moving_rock2_img, (tile_size, 25))
Mrock2_rect = moving_rock2_img.get_rect(x=500, y=500)

#instead of repeating collision detection 4 times, add the players as one varable and the rocks as one varaible 
collision_tolerance = 10
def moving_collision(players, rocks, collision_tolerance):
    if players.rect.colliderect(rocks):
        if abs(players.rect.bottom - rocks.top) < collision_tolerance: 
            players.velocityY = 0 
            players.rect.bottom = rocks.top #players can not move down when they hit the top of the rocks 
            players.onGround = True
        elif abs(players.rect.top - rocks.bottom) < collision_tolerance:
            players.velocityY = 0
            players.rect.top = rocks.bottom #players can not move up if it touches the bottom of the rock 
        elif abs(players.rect.right - rocks.left) < collision_tolerance:
            players.rect.right = rocks.left #cant move right if it hits the rocks left side 
        elif abs(players.rect.left - rocks.right) < collision_tolerance:
            players.rect.left = rocks.right #cant move left if hits the rocks right side 

#-----------------------------------------------------

#COLLECTING DIMONDS
red_dimond = pygame.image.load('./red.dimond.png')
red_dimond = pygame.transform.scale(red_dimond, (17,17))
blue_dimond = pygame.image.load('./blue.dimond.png')
blue_dimond = pygame.transform.scale(blue_dimond,(17,17))
red_dimond_list = [
    pygame.Rect(630, 80, 17, 17),
    pygame.Rect(400, 300, 17, 17),
    pygame.Rect(840, 300, 17, 17),
    pygame.Rect(100, 75, 17, 17),
    pygame.Rect(20, 350, 17, 17),
]
blue_dimond_list = [
    pygame.Rect(490, 330, 17, 17), #above + in the middle of the 2 waters. in the middle 
    pygame.Rect(840, 530, 17, 17), #above + in the middle of the 2 waters. at the bottom 
    pygame.Rect(680, 80, 17, 17), #top one
    pygame.Rect(970, 150, 17, 17), # down the side 
    pygame.Rect(50, 250, 17, 17) #left corner
]
dimond_count = 0

#-----------------------------------------------------
# GAME OVER SCREEN
#def show_game_over(screen, dimond_count):
    #font = pygame.font.Font (None, 32) #the font type and size 
    #text1 = font.render( 'Game Over', True,(255,255,255)) #the text 
    #text2 = font.render('score is', str(dimond_count), True, (255,255,255))
    #text1_rect = text1.get_rect(center= (screen_height/2, screen_height/2)) #gets the rectangle (position) of the text 
    #text2_rect = text2.get_rect(center= (screen_height/2, screen_height/2))
    #gameover_screen = screen.fill(0,0,0) 
   # screen.blit(text1, text1_rect)
    #screen.blit(text2, text2_rect)
    #pygame.display.flip()
   # pygame.time.wait(4000)
#i couldnt get the gameover screen to display so i decided to just have the game output 'game over' when the player dies. 
#used chatGPT to tell me where to put the code (now in line 399)
    
#-----------------------------------------------------
#-----------------------------------------------------
#GAME LOOP 
run = True
while run and not game_over:  # code of game keeps looping
    screen.blit(bg_img, (0, 0)) 
    screen.blit(moving_rock_img, Mrock_rect)
    screen.blit(moving_rock2_img, Mrock2_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
#-----------------------------------------------------           
#moving rocks, within the loop of the game so it is repeatitive 
    if Mrock_rect.left >=300 or Mrock_rect.left<100: #the rock will move from position 300 to 100
        platform_velocity*= -1 #reverses the direction 
    Mrock_rect.left += platform_velocity #rock continues moving in that directon until it reaches >300 and <100, appliying the speed to the movement 

    if Mrock2_rect.left >=900 or Mrock2_rect.left<500:
         platform_velocity2 *= -1
    Mrock2_rect.left += platform_velocity2
   
    #had help from chatGPT with these three lines of code
    for players in (player1, player2):
        for rocks in (Mrock_rect, Mrock2_rect):
             moving_collision(players, rocks, collision_tolerance)

#-----------------------------------------------------
#showing dimonds on the screen and removing them
    for R in red_dimond_list:
        screen.blit(red_dimond,(R[0], R[1]))
    for B in blue_dimond_list:
        screen.blit(blue_dimond,(B[0], B[1]))
    for D in blue_dimond_list[:]:
        if D.colliderect(player1):
            blue_dimond_list.remove(D)
            dimond_count+=1
    for D in red_dimond_list[:]:
        if D.colliderect(player2):
            red_dimond_list.remove(D)
            dimond_count+=1       

#-----------------------------------------------------
#lava and water colision detection  
    # Inside the game loop
    for lava in lava_group:
        if player1.rect.colliderect(lava.rect):
            game_over = True
            break  # Exit the loop as soon as a collision is detected

    for water in water_group:
        if player2.rect.colliderect(water.rect):
            game_over = True
            break  # Exit the loop as soon as a collision is detected

    for lava in lava_group:
        if player2.rect.colliderect(lava.rect):
            player2.velocityY = 0 
            player2.rect.bottom = lava.rect.top
            player2.onGround = True
            break  # Break if collision is detected

    for water in water_group:
        if player1.rect.colliderect(water.rect):
            player1.velocityY = 0 
            player1.rect.bottom = water.rect.top
            player1.onGround = True
            break  # Break if collision is detected
#-----------------------------------------------------   
#key presses 
    #player 1
    userInput1 = pygame.key.get_pressed()
    if userInput1[pygame.K_LEFT]:
        player1.move_left()
    if userInput1[pygame.K_RIGHT]:
        player1.move_right()
    if userInput1[pygame.K_DOWN]:
        player1.move_down()
    if userInput1[pygame.K_UP]:
        player1.jump()
    #player 2  
    userInput2 = pygame.key.get_pressed()
    if userInput2[pygame.K_a]:
        player2.move_left()
    if userInput2[pygame.K_d]:
        player2.move_right()
    if userInput2[pygame.K_s]:
        player2.move_down()
    if userInput2[pygame.K_SPACE]:
        player2.jump()
#-----------------------------------------------------
        if game_over:

            font = pygame.font.Font (None, 32) #the font type and size 
            text1 = font.render( 'Game Over', True,(255,255,255)) #the text 
            text2 = font.render('Score: ' + str(dimond_count), True, (255, 255, 255))
            text1_rect = text1.get_rect(center= (screen_height/2, screen_height/2 -20)) #gets the rectangle (position) of the text 
            text2_rect = text2.get_rect(center= (screen_height/2, screen_height/2)) 
            screen.blit(text1, text1_rect)
            screen.blit(text2, text2_rect)
    
            wait_time = 4000  # 4 seconds in milliseconds
            start_ticks = pygame.time.get_ticks()  # Get current ticks
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting = False
                        run = False  # Or set to False to exit the game loop
                if pygame.time.get_ticks() - start_ticks > wait_time:
                    waiting = False
                    break 
#-----------------------------------------------------
    lava_group.draw(screen)
    water_group.draw(screen)
    world.draw(screen)    
    player1.update(world)
    player1.draw(screen) 
    player2.update(world) #update the characters 
    player2.draw(screen) # Draw the character
    pygame.display.flip() # update the display
    clock.tick (60) 
    
       

#-----------------------------------------------------
#-----------------------------------------------------

pygame.quit()
sys.exit()

#if players get all the dimonds in 1min then they win (add more dimonds) - need to do 
#if they dont its gameover and they dont win 
# THE DUALITY SHOOTER GAME --> first pygame proj.

import os       # to access the files
import pygame      
pygame.font.init()        # To use the fonts lib
pygame.mixer.init()       # To be able to use music


WIDTH,HEIGHT = 900, 500     # vars for window width and height
WIN = pygame.display.set_mode((WIDTH,HEIGHT))       # set up the window
pygame.display.set_caption("First Game")        # set the  title bar caption

# defining the colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)        # the rect for the center line

# Moosick
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))
BACKROUND_MUSIC = pygame.mixer.Sound(os.path.join('Assets','bensound-epic.mp3'))

# Setting up fonts
HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)

FPS = 60
VEL=5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

# creating user events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# loading the images
YELLOW_S = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_S = pygame.transform.rotate(pygame.transform.scale(YELLOW_S,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)         # rotating by 90 and rescaling


RED_S = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_S = pygame.transform.rotate(pygame.transform.scale(RED_S,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)             

SPACE = pygame.image.load(os.path.join('Assets','space.png'))
SPACE = pygame.transform.scale(SPACE,(WIDTH,HEIGHT))

# The drawing func.
def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    WIN.blit(SPACE,(0,0))       # drawing the bg
    pygame.draw.rect(WIN,BLACK,BORDER)      # drawing the deviding line

    red_health_text = HEALTH_FONT.render("Health: "+ str(red_health),1,WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: "+ str(yellow_health),1,WHITE)
    WIN.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text,(10,10))

    # drawing the two spaceships
    WIN.blit(YELLOW_S, (yellow.x,yellow.y))
    WIN.blit(RED_S, (red.x,red.y))

    # drawing the bullets
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)  

    pygame.display.update()     # IMP.... display needs to be updated 


def yellow_handle_movement(keys_pressed,yellow):
        if keys_pressed[pygame.K_a] and yellow.x-VEL>0: #LEFT
            yellow.x-=VEL
        if keys_pressed[pygame.K_d] and yellow.x+VEL+yellow.width<BORDER.x: #RIGHT
            yellow.x+=VEL
        if keys_pressed[pygame.K_w] and yellow.y-VEL>0: #UP
            yellow.y-=VEL
        if keys_pressed[pygame.K_s] and yellow.y+VEL+yellow.height<HEIGHT-15: #DOWN
            yellow.y+=VEL

def red_handle_movement(keys_pressed,red):
        if keys_pressed[pygame.K_LEFT] and red.x-VEL>BORDER.width+ BORDER.x: #LEFT
            red.x-=VEL
        if keys_pressed[pygame.K_RIGHT] and red.x+VEL+red.width<WIDTH: #RIGHT
            red.x+=VEL
        if keys_pressed[pygame.K_UP] and red.y-VEL>0: #UP
            red.y-=VEL
        if keys_pressed[pygame.K_DOWN] and red.y+VEL+red.height<HEIGHT-15: #DOWN
            red.y+=VEL

# Func to handle bullet movements and collisions
def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x+=BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if(bullet.x>WIDTH):
            yellow_bullets.remove(bullet)
        elif bullet.x<0:
            red_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x-=BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if(bullet.x>WIDTH):
            yellow_bullets.remove(bullet)
        elif bullet.x<0:
            red_bullets.remove(bullet)

# Func to get winner text
def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text,(WIDTH//2 - draw_text.get_width()//2,HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


# CODE DRIVING FUNCTION
def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    red_bullets= []
    yellow_bullets =[]

    red_health = 10
    yellow_health =10

    winner_text=""

    clock = pygame.time.Clock() 
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            #pygame.mixer.music.set_volume(0.1)
            #ACKROUND_MUSIC.play()

            if event.type == pygame.QUIT:
                run= False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2,10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(red.x , red.y + red.height//2 - 2,10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            
            if event.type == RED_HIT:
                red_health-=1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health-=1
                BULLET_HIT_SOUND.play()
    
        if red_health<=0:
            winner_text="Yellow Wins!"

        if yellow_health<=0:
            winner_text="Red Wins!"

        if winner_text!= "":
            draw_winner(winner_text)
            break

        keys_pressed= pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)

    main()   # Rerun on completion


if __name__=="__main__":
    main()
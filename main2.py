import pygame
from pygame.locals import *
import sys
pygame.init()

frame_size_x = 800
frame_size_y = 500

FPS = 60            #Game speed (60 frames per second)  
ship_width = 55     #Spaceship width (55 pixels wide)  
ship_height = 40    #Spaceship height (40 pixels tall)  
max_num_of_bullet = 5  #Max bullets allowed on screen at once  
bullet_velocity = 7

window_screen = pygame.display.set_mode((frame_size_x, frame_size_y))


pygame.display.set_caption("Space Shooter")  # Set the window title

white = (255, 255, 255)  # RGB Code for White
black = (0, 0, 0)  # RGB Code for Black
green = (110, 194, 54)  # RGB Code for Green Bullet
blue = (23, 54, 235)  # RGB Code for Blue Bullet
border = pygame.Rect((frame_size_x // 2) - 5, 0, 10, frame_size_y)
background = pygame.transform.scale(
    pygame.image.load('multigame/gallery/sprites/background.png'),
    (frame_size_x, frame_size_y)
).convert()

space_shooter_logo = pygame.image.load('multigame/gallery/sprites/space_shooter.png').convert_alpha()

space_shooter_logo = pygame.transform.scale(space_shooter_logo, (290, 150)) ##di scale jadi ukuran 300 dan 150

green_ship_img = pygame.transform.rotate(pygame.image.load('multigame/gallery/sprites/shipGreen.png'), 270)
blue_ship_img = pygame.transform.rotate(pygame.image.load('multigame/gallery/sprites/shipBlue.png'), 90)
green_ship = pygame.transform.scale(green_ship_img, (ship_width, ship_height)).convert_alpha()
blue_ship = pygame.transform.scale(blue_ship_img, (ship_width, ship_height)).convert_alpha()

bullet_fire_sound = pygame.mixer.Sound('multigame/gallery/audio/sfx_fire.ogg')
#TEST
def handle_bullets(green_bullets, blue_bullets, green, blue):
    for bullet in green_bullets:
        bullet.x += bullet_velocity
        if blue.colliderect(bullet):
            green_bullets.remove(bullet)
        elif bullet.x > frame_size_x:
            green_bullets.remove(bullet)
    for bullet in blue_bullets:
        bullet.x -= bullet_velocity
        if green.colliderect(bullet):
            blue_bullets.remove(bullet)
        elif bullet.x < 0:
            blue_bullets.remove(bullet)  


def main():
    clock = pygame.time.Clock()
    green_rect = pygame.Rect(100,100, ship_width, ship_height)
    blue_rect = pygame.Rect(700,300, ship_width, ship_height)
    green_bullets = []
    blue_bullets = []
    
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.exit()
                sys.exit()
            if(event.type == pygame.KEYDOWN):
                if event.key == pygame.K_LCTRL and len(green_bullets)<max_num_of_bullet:
                    bullet = pygame.Rect(green_rect.x + green_rect.width, green_rect.y + green_rect.height // 2, 10, 5)
                    green_bullets.append(bullet)   
                    bullet_fire_sound.play()
                if event.key == pygame.K_RCTRL and len(blue_bullets)< max_num_of_bullet:
                    bullet = pygame.Rect(blue_rect.x, blue_rect.y + blue_rect.height // 2,  10, 5)
                    blue_bullets.append(bullet) 
                    bullet_fire_sound.play()
        print(green_bullets, blue_bullets)
        handle_bullets(green_bullets, blue_bullets, green_rect, blue_rect)
        window_screen.blit(background, (0, 0)) #blit the background
        pygame.draw.rect(window_screen, black, border)
        window_screen.blit(green_ship, (green_rect.x, green_rect.y))
        window_screen.blit(blue_ship, (blue_rect.x, blue_rect.y))
        for bullet in green_bullets:
            pygame.draw.rect(window_screen, green, bullet)  # Draw Green Bullets
        for bullet in blue_bullets:
            pygame.draw.rect(window_screen, blue, bullet) # Draw Blue Bullets
        pygame.display.update()  # Update Screen

def welcome_screen(): #our welcome screen
    while True:
        window_screen.blit(background, (0, 0)) #munculin background
        window_screen.blit(space_shooter_logo, (frame_size_x//3, 40))#munculin logo
        welcome_font = pygame.font.SysFont("impact", 24)#font
        welcome_text = welcome_font.render("Press Any Key To Begin...", 1, white)#text di awal
        window_screen.blit(welcome_text, (frame_size_x // 2 - welcome_text.get_width() //2, frame_size_y // 2 - welcome_text.get_height() // 2)) 
        for event in pygame.event.get():
           if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
              pygame.quit()
              sys.exit()
           if event.type == pygame.KEYDOWN:
                print("Start the game")
                main()
        pygame.display.update()  # Update the display to show the welcome screen
    
welcome_screen()  # Call the welcome screen function to display it


#####last load the sprite

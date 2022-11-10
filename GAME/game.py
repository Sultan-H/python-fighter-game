import pygame
from fighterClass import Fighter

pygame.init()

#game window
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FIGHT AND WIN")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#load background image
bg_image = pygame.image.load("assets/background/pixel_bg_cliffs.png").convert_alpha()

#drawing background function
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0, 0))

#create two instances of fighters
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

#game loop
run = True
while run:
    
    clock.tick(FPS)

    #draw background
    draw_bg()

    #move fighters
    fighter_1.move(screen_width, screen_height)

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event handler --> close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #update display
    pygame.display.update()

pygame.quit()

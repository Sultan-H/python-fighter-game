import pygame

#fighter class
class Fighter():
    def __init__(self,x,y):
        self.rect = pygame.Rect((x, y, 80, 100))
        self.vel_y = 0
        self.jump = False

    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        speed = 8
        gravity = 2
        dx = 0
        dy = 0
        floor = 35

        #get keypresses
        key = pygame.key.get_pressed()

        #movement
        if key[pygame.K_a]:
            dx = -speed
        if key[pygame.K_d]:
            dx = speed
        #jump
        if key[pygame.K_w] and self.jump == False:
            self.vel_y = -30
            self.jump = True
        #attack
        #if key[pygame.K_r] or key[pygame.K_t]:

            #determine which attack type was used


        #apply gravity
        self.vel_y += gravity
        dy += self.vel_y

        #ensure player stays on screen
        if self.rect.left + dx < 0:
            dx =- self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right
        if self.rect.bottom + dy > SCREEN_HEIGHT - floor:
            self.vel_y = 0
            self.jump = False
            dy = SCREEN_HEIGHT - floor - self.rect.bottom

        #update player position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
import pygame, sys

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255,255,255)
black = (0, 0, 0)
purple = (127, 0, 255)
orange = (255, 165, 0) 
gray = (192,192,192)

class Player(pygame.sprite.Sprite): #animation class 
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('frame_0.png'))
        self.sprites.append(pygame.image.load('frame_1.png'))
        self.sprites.append(pygame.image.load('frame_2.png'))
        self.sprites.append(pygame.image.load('frame_3.png'))
        self.sprites.append(pygame.image.load('frame_4.png'))
        self.sprites.append(pygame.image.load('frame_5.png'))
        self.sprites.append(pygame.image.load('frame_6.png'))
        self.sprites.append(pygame.image.load('frame_7.png'))
        self.sprites.append(pygame.image.load('frame_8.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True 


    def update(self):
        if self.is_animating == True:
            self.current_sprite += .5 # adjust this number for animation speed 
            if self.current_sprite >=len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]


pygame.init()
clock = pygame.time.Clock()
screen_width = 1440
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font('freesansbold.ttf', 16)
pygame.display.set_caption("PUSH ME!!!")


moving_sprites = pygame.sprite.Group()
player = Player(450,150) # position of player 
moving_sprites.add(player)

# score 
score_value = 0 
font = pygame.font.Font('freesansbold.ttf',32)
scoreX = 10 
scoreY = 10

def show_score(x,y):
    score = font.render("Pumpkins: " + str(score_value), True, white)
    screen.blit(score, (x,y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            score_value += 1
            player.animate()
            
    screen.fill((black))    
    show_score(scoreX,scoreY)
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)
   

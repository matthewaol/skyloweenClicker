import pygame, sys

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255,255,255)
black = (0, 0, 0)
purple = (204, 0, 204)
orange = (255, 165, 0) 
gray = (192,192,192)

#animation classes
class Pumpkin(pygame.sprite.Sprite): 
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        for i in range(0, 8): #sick ass for loop man
            image = pygame.image.load("animations/"+f"pframe_{i}.png")
            self.sprites.append(image)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True 

    def update(self):
        if self.is_animating == True:
            self.current_sprite += .55 # adjust this number for animation speed 
            if self.current_sprite >=len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]

class Scream(pygame.sprite.Sprite): 
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        for i in range(0, 7): #sick ass for loop man
            image = pygame.image.load("animations/"+f"sframe_{i}.png")
            scaled_image = pygame.transform.scale(image, (200,200))
            self.sprites.append(scaled_image)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True 

    def update(self):
        if self.is_animating == True:
            self.current_sprite += .1 # adjust this number for animation speed 
            if self.current_sprite >=len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]

class Bat(pygame.sprite.Sprite): 
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        for i in range(0, 4): #sick ass for loop man
            image = pygame.image.load("animations/"+f"bframe_{i}.png")
            scaled_image = pygame.transform.scale(image, (250,250))
            self.sprites.append(scaled_image)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True 

    def update(self):
        if self.is_animating == True:
            self.current_sprite += .1 # adjust this number for animation speed 
            if self.current_sprite >=len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]

class s_Pumpkins(pygame.sprite.Sprite): 
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        for i in range(0, 7): #sick ass for loop man
            image = pygame.image.load("animations/"+f"psframe_{i}.png")
            scaled_image = pygame.transform.scale(image, (250,250))
            self.sprites.append(image)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True 

    def update(self):
        if self.is_animating == True:
            self.current_sprite += .1 # adjust this number for animation speed 
            if self.current_sprite >=len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]

# pygame parameters 
pygame.init()
clock = pygame.time.Clock()
screen_width = 1440
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PUSH ME!!!")

# sprites 
moving_sprites = pygame.sprite.Group()
Pumpkin = Pumpkin(450,160) # position of pumpking 
moving_sprites.add(Pumpkin)

moving_sprites2 = pygame.sprite.Group()
Scream1 = Scream(50,100)
moving_sprites2.add(Scream1)

moving_sprites3 = pygame.sprite.Group()
Bat1 = Bat(1200,90) # position of bat 
moving_sprites3.add(Bat1)

moving_sprites4 = pygame.sprite.Group()
s_Pumpkins1 = s_Pumpkins(5,550)
s_Pumpkins2 = s_Pumpkins(900,550) # position of pumpkins 
moving_sprites4.add(s_Pumpkins1)
moving_sprites4.add(s_Pumpkins2)


# score 
score_value = 0 
font = pygame.font.Font('slkscre.ttf',75)
font_L = pygame.font.Font('slkscre.ttf',85)
scoreX = 460
scoreY = 20

def show_score(x,y):
    screen.blit(font.render("Pumpkins:", True, orange), (x, y)) #printing pumpkins:
    score = font_L.render(str(score_value), True, white)
    screen.blit(score, (x + 175, y + 90)) #printing the score

# background
background = pygame.image.load('background2.png') #choice of background1 or background 2
scaled_background = pygame.transform.scale(background, (1440, 800))

while True:
    screen.blit(scaled_background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            score_value += 1
            Pumpkin.animate()
        if score_value % 5 == 0: 
            s_Pumpkins1.animate()
            s_Pumpkins2.animate()

    show_score(scoreX,scoreY)
    moving_sprites.draw(screen)
    moving_sprites2.draw(screen)
    moving_sprites3.draw(screen)
    moving_sprites4.draw(screen)
    moving_sprites.update()
    moving_sprites2.update()
    moving_sprites3.update()
    moving_sprites4.update()
    Scream1.animate()
    Bat1.animate()
    pygame.display.flip()
    clock.tick(60)
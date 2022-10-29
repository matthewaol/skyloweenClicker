import pygame
pygame.init()

#colors 
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255,255,255)
black = (0, 0, 0)
purple = (127, 0, 255)
orange = (255, 165, 0) 
gray = (192,192,192)

screen = pygame.display.set_mode([1440, 800]) # setting screen size and caption
pygame.display.set_caption('csc clicker') 

background = white 
framerate = 60 
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

#game variables
green_value = 1 
red_value = 2 
gray_value = 3
purple_value = 4
blue_value = 5

draw_green = False
draw_red = False
draw_gray = False
draw_purple = False 
draw_blue = False 

length_green = 0
length_red = 0 
length_gray = 0 
length_purple = 0 
length_blue = 0

speed_green = 5
speed_red = 4
speed_gray = 3
speed_purple = 2
speed_blue = 1

score = 0
def draw_task(color, y_coord, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed 
    elif length >= 200:
        draw = False 
        length = 0
        score += value 

    task = pygame.draw.circle(screen, color, (30, y_coord), 20, 5)  #constructing the ui
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, white, [75, y_coord - 10, 190,20])

    pygame.draw.rect(screen, color, [70, y_coord-15, length, 30])

    value_text = font.render(str(value), True, black)
    screen.blit(value_text, [25, y_coord - 10])
    return task, length, draw 

def draw_score(color, y_coord, score, draw, length, speed):
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])

running = True 
while running: 
    timer.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if task1.collidepoint(event.pos):
                draw_green = True 
            if task2.collidepoint(event.pos):
                draw_red = True 
            if task3.collidepoint(event.pos):
                draw_gray = True 
            if task4.collidepoint(event.pos):
                draw_purple = True 
            if task5.collidepoint(event.pos):
                draw_blue = True
    
    screen.fill(background)
    task1, length_green, draw_green = draw_task(green, 50, green_value, draw_green, length_green, speed_green)
    task2, length_red, draw_red = draw_task(red, 100, red_value, draw_red, length_red, speed_red)
    task3, length_gray, draw_gray = draw_task(gray, 150, gray_value, draw_gray, length_gray,speed_gray)
    task4, length_purple, draw_purple = draw_task(purple, 200, purple_value, draw_purple, length_purple, speed_purple)
    task5, length_blue, draw_blue = draw_task(blue, 250, blue_value, draw_blue, length_blue, speed_blue)

    draw_score(gray, 150, gray_value, draw_gray, length_gray,speed_gray)

    pygame.display.flip()
 
pygame.quit()
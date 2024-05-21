import pygame
import random
import os

mylines = []
undolines = []

pygame.init()

clock = pygame.time.Clock()
refresh_rate = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

x = random.randint(0, SCREEN_WIDTH)
y = random.randint(0, SCREEN_HEIGHT)
vx, vy = (random.randint(100, 600) / 100), (random.randint(100, 600) / 100)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('The Experiment of Art Creation')

run = True

randy = random.randint(0,SCREEN_HEIGHT)
randx = random.randint(0,SCREEN_WIDTH)

start_pos = (0,0)
end_pos = (0,0)

space = False
hide_grid = False

grid_reference = pygame.image.load(os.path.normpath(f"{os.path.dirname(__file__)}/gridreference.png"))

while run:
    screen.fill((0,0,0))
    screen.blit(grid_reference, (0,0))
    if hide_grid:
        screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space = True
                start_pos = (square.x, square.y)
            if event.key == pygame.K_z:
                if len(mylines) > 0:
                    undolines.append(mylines[-1])
            if event.key == pygame.K_h:
                hide_grid = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space = False
                end_pos = (square.x, square.y)
                #print(square.x, square.y)
            if event.key == pygame.K_h:
                hide_grid = False

    num_lines = len(mylines)
    keys = pygame.key.get_pressed()

    myFont = pygame.font.SysFont("Times New Roman", 18)

    square = pygame.draw.rect(screen, (0,0,255), (x, y, 5, 5))

    if x > SCREEN_WIDTH:
        vx = -abs(random.randint(100, 600) / 100)
    
    match space:
        case True:
            pygame.draw.line(screen, "white", start_pos, (square.x, square.y))
            stat = myFont.render(f"You DECIDED to start at: {start_pos}", 1, (255, 255, 0))
        case False:
            myline = pygame.draw.line(screen, "white", start_pos, end_pos)
            mylines.append([start_pos, end_pos])
            stat = myFont.render(f"You DECIDED to end at: {end_pos}", 1, (255, 255, 0))

    if x < 0:
        vx = abs(random.randint(100, 600) / 100)

    if y > SCREEN_HEIGHT:
        vy = -abs(random.randint(100, 600) / 100)
    if y < 0:
        vy = abs(random.randint(100, 600) / 100)

    x += vx
    y += vy

    for l in mylines:
        pygame.draw.line(screen, "white", l[0], l[1])
    for l in undolines:
        pygame.draw.line(screen, "black", l[0], l[1]) # pseudo-erasing the lines

    screen.blit(stat, (520, 20))
    
    clock.tick(refresh_rate)
    pygame.display.flip()
pygame.quit()
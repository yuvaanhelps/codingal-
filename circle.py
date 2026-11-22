import pygame
pygame.init()
# create display surface objectof specific dimension
screen = pygame.display.set_mode((400, 400))
#fill the screen with white colour
screen.fill((255, 255, 255))
# define colours
green=(0, 255, 0)
# draw a solid circle
pygame.draw.circle(screen, green, (300, 300), 50)
# draw outlined circle
pygame.draw.circle(screen, green, (100, 100), 50, 3)
# draw the surface object to the screen
pygame.display.update()
#game loop
running=True
while running:
    #event handling
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
#quit pygame
pygame.quit()

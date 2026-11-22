import pygame
pygame.init()
screen = pygame.display.set_mode((400, 500))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,255), pygame.Rect(50, 50, 100, 100))
    pygame.display.flip()
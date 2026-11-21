#import necessary libraries
import pygame
#initilize necessary modules
pygame.init()
# set up window geometry
screen= pygame.display.set_mode((400,500))
# create a loop to run till the user quits the game
done = False
while not done:
    # cleare the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # make the chages visible
    pygame.display.update()        
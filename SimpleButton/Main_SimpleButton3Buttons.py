#  pygame SimpleButton  3-Button test

# 1 - Import packages
import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# Define constants
BACKGROUND_COLOR = (245, 245, 245)

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
FRAMES_PER_SECOND = 30 

# 2 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
# Create instances of SimpleButton
oButtonA = SimpleButton(window, (75, 80), 
                        'images/buttonAUp.png', 
                        'images/buttonADown.png')
oButtonB = SimpleButton(window, (250, 80),
                        'images/buttonBUp.png', 
                        'images/buttonBDown.png')
oButtonC = SimpleButton(window, (425, 80), 
                        'images/buttonCUp.png', 
                        'images/buttonCDown.png')

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to each button, see if one has been clicked
        if oButtonA.handleEvent(event):
            print('User clicked button A.')
        elif oButtonB.handleEvent(event):
            print('User clicked button B.')
        elif oButtonC.handleEvent(event):
            print('User clicked button C.')

    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BACKGROUND_COLOR)
    
    # 10 - Draw all window elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

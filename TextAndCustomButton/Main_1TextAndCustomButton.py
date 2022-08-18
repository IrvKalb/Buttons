#  pygame TextButton and CustomButton  Button test

# 1 - Import packages
import pygame
from pygame.locals import *
import pygwidgets
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
# Create an instance of TextButton
oButton = pygwidgets.TextButton(window, (75, 80), 'Button')

# Create an instance of CustomButton
oOkButton = pygwidgets.CustomButton(window, (75, 200),
                        up='images/okUp.png',
                        down='images/okDown.png',
                        over='images/okOver.png',
                        disabled='images/okDisabled.png')


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to each button, see if one has been clicked
        if oButton.handleEvent(event):
            print('User clicked button the Text Button.')

        elif oOkButton.handleEvent(event):
            print('User clicked on the OK Button.')

    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BACKGROUND_COLOR)
    
    # 10 - Draw all window elements
    oButton.draw()
    oOkButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

#  pygame TextButton and CustomButton  3-Button test

# 1 - Import packages
import pygame
from pygame.locals import *
import pygwidgets
import sys

# Define constants
BACKGROUND_COLOR = (245, 245, 245)
RED = (255, 0, 0)
BLUE = (135, 206, 250)
LIGHT_GREEN=(144,238,144)
PINK = (255,192,203)
PEACH = (255,218,185)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
FRAMES_PER_SECOND = 30 

# 2 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
# Create instances of TextButton
oButtonA = pygwidgets.TextButton(window, (75, 80), 'Button A')
oButtonB = pygwidgets.TextButton(window, (250, 80), 'Button B',
                                 fontName='Courier', fontSize=24,
                                 textColor=RED, upColor=LIGHT_GREEN, overColor=PINK, downColor=PEACH)
oButtonC = pygwidgets.TextButton(window, (425, 80), 'Button C', upColor=BLUE,
                                 width=160, height = 50, fontSize=28, fontName='Arial')

# Create instances of CustomButton
oOkButton = pygwidgets.CustomButton(window, (75, 200),
                        up='images/okUp.png',
                        down='images/okDown.png',
                        over='images/okOver.png',
                        disabled='images/okDisabled.png')
oContinueButton = pygwidgets.CustomButton(window, (250, 200),
                        up='images/continueUp.png',
                        down='images/continueDown.png',
                        over='images/continueOver.png',
                        disabled='images/continueDisabled.png')
oRestartButton = pygwidgets.CustomButton(window, (425, 200),
                        up='images/restartUp.png',
                        down='images/restartDown.png',
                        over='images/restartOver.png',
                        disabled='images/restartDisabled.png')

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
        elif oOkButton.handleEvent(event):
            print('User clicked on OK.')
        elif oContinueButton.handleEvent(event):
            print('User clicked on Continue.')
        elif oRestartButton.handleEvent(event):
            print('User clicked on Restart.')

    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BACKGROUND_COLOR)
    
    # 10 - Draw all window elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()
    oOkButton.draw()
    oContinueButton.draw()
    oRestartButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

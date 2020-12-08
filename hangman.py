#Import 2 libraries to the game
import pygame
import random
#Initialize pygame (game,loop, game scene
pygame.init()
winHeight = 480
winWidth = 700
GREEN = (0,255,0)

#Create window game
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hangman by Daniel")

#Main program
#Create a game loop to keep the game visible
inPlay = True
while inPlay:
    win.fill(GREEN) #makes window backgroubd colour GREEN
    pygame.display.update()
    pygame.display.delay(100)

#Quit the pygame
pygame.quit()

"""Using pygame to see the sorting  dynamically. """

'''This code requires the 'BubbleSort.py' file to be in the same directory '''

### Sahil Islam ###
### 13/06/2020 ###

from BubbleSort import *
import numpy as np
import pygame

pygame.init()

display_width = 900
display_height = 650

black = [0, 0, 0]
white = [255, 255, 255]
red = [200, 0, 0]

display_surface = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Bubble Sort")


def rect(x, y, rectHeight, color):
    rectWidth = 10

    pygame.draw.rect(display_surface, color, [x, y, rectWidth, rectHeight])


display_surface.fill(white)
n = 100
x = np.linspace(0, display_width, n, endpoint=False)
rectHeight = np.zeros(n)

for i in range(n):
    rectHeight[i] = np.random.randint(0, display_height)

for i in range(len(x)):
    rect(x[i], display_height - rectHeight[i], rectHeight[i], black)

for i in range(len(x)):
    oneDSort(rectHeight)

    rect(x[i], display_height - rectHeight[i], rectHeight[i], red)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()

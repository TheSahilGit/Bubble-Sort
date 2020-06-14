from BubbleSort import *
import numpy as np
import pygame

pygame.init()

width = 900
height = 650

black = [0, 0, 0]
white = [255, 255, 255]
red = [200, 0, 0]

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Bubble Sort")


def rect(x, h, color):
    w = 10
    pygame.draw.rect(screen, color, [x, height - h, w, h])


w = 10
n = int(width / w)
h = np.random.randint(10, height, n)
x = np.linspace(0, width, n)

screen.fill(white)

for i in range(len(h)):
    rect(x[i], h[i], black)

while True:
    for i in range(len(h)):

        oneDSort(h)
        rect(x[i], h[i], red)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(10)

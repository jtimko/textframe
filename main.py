#!/usr/bin/env python3

import pygame

pygame.init()
x = 1080/2
y = 1920/2

screen = pygame.display.set_mode((y, x))
pygame.display.set_caption("Picture Frame!")

img = pygame.image.load("img/me.jpg")
img = pygame.transform.scale(img, (x, y))
img = pygame.transform.rotate(img, 90)

screen.blit(img, (0, 0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
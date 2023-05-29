#!/usr/bin/env python3

import pygame

class PictureFrame:

    def __init__(self):
        self.x = 1080/2
        self.y = 1920/2
        self.screen = pygame.display.set_mode((self.y, self.x))

    def load_image(self, image):
        self.img = pygame.image.load(image)
        self.img = pygame.transform.scale(self.img, (self.x, self.y))
        self.img = pygame.transform.rotate(self.img, 90)

    def display_image(self):
        self.screen.blit(self.img, (0, 0))
        pygame.display.flip()

picture = PictureFrame()
picture.load_image("img/me.jpg")
picture.display_image()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                picture.load_image("img/you.png")
                picture.display_image()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)



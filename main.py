#!/usr/bin/env python3

import pygame
import os

# Created a picture frame class that will display an image on the screen. Pygame is used to provide the window.
class PictureFrame:
    def __init__(self):
        self.path = os.getcwd() + '/img/'
        self.x = 1080/2
        self.y = 1920/2
        self.screen = pygame.display.set_mode((self.y, self.x))
        self.current = sorted(filter(os.path.isfile, map(self.get_latest_file, os.listdir(self.path))), key=os.path.getctime, reverse=True)

    def load_image(self):
        self.img = pygame.image.load(self.current[0])
        self.img = pygame.transform.scale(self.img, (self.x, self.y))
        self.img = pygame.transform.rotate(self.img, 90)

    def display_image(self):
        self.screen.blit(self.img, (0, 0))
        pygame.display.flip()

    def check_for_updates(self):
        self.check = sorted(filter(os.path.isfile, map(self.get_latest_file, os.listdir(self.path))), key=os.path.getctime, reverse=True)

    def get_latest_file(self, item):
        if not item.startswith('.'):
            return self.path + item
        else:
            return ''

# The execution of the program starts here.
picture = PictureFrame()
picture.load_image()
picture.display_image()

while True:
    picture.check_for_updates()
    
    for event in pygame.event.get():
        if picture.check[0] != picture.current[0]:
            picture.current = picture.check
            picture.load_image()
            picture.display_image()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)



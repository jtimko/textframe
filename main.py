#!/usr/bin/env python3

import pygame
import os
from twilio.rest import Client


# Testing twilio. Will involve listening for a mms message and then displaying the image on the screen.

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='' + os.environ['TWILIO_FROM'],
    body='Hello there!',
    to='' + os.environ['TWILIO_TO']
)

print(message.sid)

# Created a picture frame class that will display an image on the screen. Pygame is used to provide the window.

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

# The execution of the program starts here.
picture = PictureFrame()
picture.load_image("img/me.jpg")
picture.display_image()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                picture.load_image("img/you.jpg")
                picture.display_image()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)



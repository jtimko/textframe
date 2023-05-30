#!/usr/bin/env python3

import pygame
import server
import multiprocessing
import time
from pictureframe import PictureFrame


# The execution of the program starts here.

def run_server():
    server.start_server()

def run_picture_frame():
    picture = PictureFrame()
    picture.load_image()
    picture.display_image()

    while True:
        picture.check_for_updates()
        if picture.check[0] != picture.current[0]:
            picture.current = picture.check
            time.sleep(3)
            picture.load_image()
            picture.display_image()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

if __name__ == '__main__':
    # p = multiprocessing.Process(target=run_server)
    # p.start()
    run_picture_frame()


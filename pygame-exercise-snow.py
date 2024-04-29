# Snowflake Practice
# Edan was here :)
# Apr 29th 

import pygame as pg
import random

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)


class Snowflake(pg.sprite.Sprite):
    def __init__(self, size: int):
        super().__init__()
        self.image = pg.image.load("./Images/snowy.png")
        self.rect = self.image.get_rect()

        # Spawn in a random location in the view
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = 0

        self.vel_x = 0
        self.vel_y = random.choice([3, 4, 5, 6, 7, 8])

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    pg.display.set_caption("Snowflake Practice by Edan")

    snowy = Snowflake(5)


    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Add one snowflake to the sprite group
    all_sprites.add(snowy)

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        # Update the location of EVERY SPRITE
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw()

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
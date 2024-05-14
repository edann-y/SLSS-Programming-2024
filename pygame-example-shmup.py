# Shmup
# Edan was Here :)

import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH = 1000  # Pixels
HEIGHT = 1400
SCREEN_SIZE = (WIDTH, HEIGHT)
TITLE = "Shoot Em' Up"

# Make Player Class to move only x
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/nobgmonkey.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = 1300

class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        super().__init__()

        self.image = pg.Surface((20, 50))
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()

        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]
        


# Make Bullets 
# Make Enemies

def start():
    """Environment Setup and Game Loop"""

    pg.init()
    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # Variables not groups
    player = Player()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    all_sprites.add(player)

    pg.display.set_caption("Shoot Em' Up")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                all_sprites.add(Bullet((player.rect.centerx, player.rect.top)))


        # --- Update the world state
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)
        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
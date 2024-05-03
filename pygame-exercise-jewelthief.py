# Jewel Thief
# Edan was Here :)

import random
import pygame as pg

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1920
HEIGHT = 1080
TITLE = "Jewel Thief"

NUM_BANANA = 1


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/nobgmonkey.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = pg.mouse.get_pos()[1]

class Banana(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/banana.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

def main():
    pg.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pg.time.Clock()

    player = Player()
    bananas = Banana

    # Create a group of sprites
    all_sprites = pg.sprite.Group()

    banana_sprites = pg.sprite.Group()

    # Add the DVD Logo object to the group of sprites
    all_sprites.add(player)
    all_sprites.add(bananas)
    banana_sprites.add(bananas)

    for _ in range(NUM_BANANA):
        bananas = Banana()

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        # Update the location of EVERY SPRITE
        all_sprites.update()

        # Collsion System
        bananacollision = pg.sprite.spritecollide(player, banana_sprites, False)

        for bananas in bananacollision:
            print(f"Monke ate Banana at {bananas.rect.x}, {bananas.rect.y}")

        screen.fill(BLACK)
        all_sprites.draw(screen)

        # ----- UPDATE DISPLAY
        pg.display.flip()
        clock.tick(60)

    pg.quit()


def random_coords():
    x, y = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    return x, y


if __name__ == "__main__":
    main()
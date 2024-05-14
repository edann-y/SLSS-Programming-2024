# Jewel Thief
# Edan was Here :)

import random
import pygame as pg

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
NUM_BANANA = 5


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
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

class Gorilla(pg.sprite.Sprite):
    """Represents DVD logo sprite"""

    def __init__(self):
        super().__init__()
        # image - Visual Representation
        self.image = pg.image.load("./Images/gorilla.png")

        self.rect = self.image.get_rect()

                # Spawn in a random location in the view
        self.rect.x = 0
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

        self.vel_x = random.choice([-6, -5, -4, -3, 3, 4, 5, 6])
        self.vel_y = random.choice([-6, -5, -4, -3, 3, 4, 5, 6])


    def update(self):
        # Update the location of the DVD logo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bounce if reaches bottom
        # if the bottom of the sprite is past the bottom of screen
        # convert to negative (*-1)
        if self.rect.bottom > HEIGHT:
            self.vel_y *= -1
        
        # Top
        if self.rect.top < 0:
            self.vel_y *= -1

        # Left

        if self.rect.left < 0:
            self.vel_x *= -1

        # Right
        if self.rect.right > WIDTH:
            self.vel_x *= -   1

def start():
    pg.init()
    pg.mouse.set_visible(False)

    # ----- SCREEN PROPERTIES
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0

    life = 5

    font = pg.font.SysFont("Futura", 24)

    player = Player()

    gorilla = Gorilla()

    # Create a group of sprites
    all_sprites = pg.sprite.Group()

    banana_sprites = pg.sprite.Group()

    enemy_sprite = pg.sprite.Group()

    enemy_sprite.add(gorilla)

    all_sprites.add(gorilla)

    # Add the DVD Logo object to the group of sprites
    for _ in range(NUM_BANANA):
        bananas = Banana()
        all_sprites.add(bananas)
        banana_sprites.add(bananas)

    all_sprites.add(player)

    pg.display.set_caption("Monkey Game")

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
        bananacollision = pg.sprite.spritecollide(player, banana_sprites, True)

        gorillacollision = pg.sprite.spritecollide(player, enemy_sprite, False)

        for bananas in bananacollision:
            score += 1

            print(f"Hunger: {score}")

        # if no more banana (no good :c), respawn for monke
        if len(banana_sprites) <= 0:
            for _ in range(NUM_BANANA):
                bananas = Banana()
                all_sprites.add(bananas)
                banana_sprites.add(bananas)

        for gorilla in gorillacollision:
            life -= (1 / 60)

        screen.fill(BLACK)
        all_sprites.draw(screen)

        score_image = font.render(f"Score: {score}",  True, SKY_BLUE)
        screen.blit(score_image, (5, 5))

        lives_image = font.render(f"Lives Remaining: {int(life)}",  True, SKY_BLUE)
        screen.blit(lives_image, (5, 35))

        # ----- UPDATE DISPLAY
        pg.display.flip()
        clock.tick(60)

        if life <= 0:
            pg.quit()

    pg.quit()


def main():
    start()


if __name__ == "__main__":
    main()
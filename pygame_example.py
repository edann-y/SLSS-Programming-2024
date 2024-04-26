# Pygame Boilerplate

import pygame
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


class Monke(pygame.sprite.Sprite):
    """Represents DVD logo sprite"""

    def __init__(self):
        super().__init__()
        # image - Visual Representation
        self.image = pygame.image.load("./Images/nobgmonkey.png")

        # rect - Hitbox Representation
        # get_rect() -> Rect
        # Sets x and y to 0, width and height to image
        self.rect = self.image.get_rect()

                # Spawn in a random location in the view
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
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
    """Environment Setup and Game Loop"""

    pygame.init()

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    pygame.display.set_caption("DVD Logo Screensaver")

    dvdlogo = Monke()

    # Create a group of sprites
    all_sprites = pygame.sprite.Group()

    # Add the DVD Logo object to the group of sprites
    all_sprites.add(dvdlogo)

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    all_sprites.add(Monke())

        # --- Update the world state
        # Update the location of EVERY SPRITE
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        # Draw all the sprites on the screen
        all_sprites.draw(screen)

        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
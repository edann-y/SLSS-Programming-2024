# Pygame Boilerplate

import pygame

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



def start():
    """Environment Setup and Game Loop"""

    pygame.init()

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

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    pygame.display.set_caption("Monke")

    # Make a monke logo object 
    monkey = Monke()

    # Move the Monkey to the middle 
    monkey.rect

    # Create a group of sprites
    all_sprites = pygame.sprite.Group()

    # Add the DVD Logo object to the group of sprites
    all_sprites.add(monkey)

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Update the world state

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
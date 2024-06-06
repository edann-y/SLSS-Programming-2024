# Shmup
# Edan was Here :)

import random as ran
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

# Make Player Class to move only x + Bullets
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

        self.vel_y = -7

    def update(self):
        self.rect.y += self.vel_y

        if self.rect.top < 0:
            self.kill()
        
# Make Enemies
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/gorilla.png")
        self.rect = self.image.get_rect()

        self.rect.x = ran.randrange(0, WIDTH - self.rect.width)
        self.rect.y = 0

        self.vel_x = ran.choice([-6, -5, -4, -3, 3, 4, 5, 6])
        self.vel_y = 2

    
    def update(self):
        # Update the location of the DVD logo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bounce if reaches bottom
        # if the bottom of the sprite is past the bottom of screen
        # convert to negative (*-1)
    
        if self.rect.left < 0:
            self.vel_x *= -1

        # Right
        if self.rect.right > WIDTH:
            self.vel_x *= -   1
    

def start():
    pg.init()
    pg.mouse.set_visible(False)

    score = 0
    life = 5

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # Variables not groups
    player = Player()
    all_sprites = pg.sprite.Group()
    enemy_sprite = pg.sprite.Group()
    bullet_sprite = pg.sprite.Group()

    all_sprites.add(player)

    # Create enemies
    for _ in range(1):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_sprite.add(enemy)

    pg.display.set_caption("Shoot Em' Up")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                bullet = Bullet((player.rect.centerx, player.rect.top))
                all_sprites.add(bullet)
                bullet_sprite.add(bullet)

        # --- Collision Detection ---
        # Check for collisions between bullets and enemies
        hits = pg.sprite.groupcollide(bullet_sprite, enemy_sprite, True, True)
        for hit in hits:
            # Increase score or do other actions when a hit occurs
            score += 1

            # Create a new enemy after one is destroyed
            enemy = Enemy()
            all_sprites.add(enemy)
            enemy_sprite.add(enemy)

        enemycollision = pg.sprite.spritecollide(player, enemy_sprite, False)

        for enemy in enemycollision:
            life -= (1 / 60)

        if life < 0:
            pg.quit()

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
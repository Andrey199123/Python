import math
from math import floor
import pygame as pg
import pygame.sprite

pg.init()
screen = pg.display.set_mode((1460, 900))
pg.display.set_caption("Earth")
clock = pg.time.Clock()


# Functions
class Merc(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.sprites = [pygame.image.load("Mercedes8.png"), pygame.image.load("Mercedes7.png"),
                        pygame.image.load("Mercedes6.png"), pygame.image.load("Mercedes5.png"),
                        pygame.image.load("Mercedes4.png"), pygame.image.load("Mercedes3.png"),
                        pygame.image.load("Mercedes2.png"), pygame.image.load("Mercedes1.png")]
        for value in self.sprites:
            self.sprites[self.counter] = pg.transform.rotozoom(value, 90, 0.5)
            self.counter += 1
        self.counter = 0
        for value in self.sprites:
            self.sprites[self.counter] = pg.transform.flip(value, True, False)
            self.counter += 1
        self.counter = 0
        self.current_sprite = 0
        self.original_image = self.sprites[self.current_sprite]
        self.image = self.sprites[self.current_sprite]
        self.xradius = 657
        self.yradius = 405
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
        self.correction_angle = 0

    def update(self, deg):
        deg = 360 - deg
        self.image = self.sprites[floor(self.current_sprite)]
        self.current_sprite += 0.5
        self.current_sprite = self.current_sprite % 8
        self.x = int(math.cos(deg * 2 * math.pi / 360) * self.xradius) + 657
        self.y = int(math.sin(deg * 2 * math.pi / 360) * self.yradius) + 405
        dx, dy = 657 - self.x, 405 - self.y
        angle = math.degrees(math.atan2(-dy, dx)) - self.correction_angle
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=(self.x + 50, self.y + 50))
        screen.blit(self.image, self.rect)


class Ellipse(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((1460, 900))
        self.image.fill("White")
        pg.draw.ellipse(self.image, (255, 255, 0), (0, 0, 1460, 900), width=7)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.mask = pygame.mask.from_surface(self.image)


# Variables
ellipse, mercedes_class, degree = pg.sprite.GroupSingle(
    Ellipse()), pg.sprite.GroupSingle(Merc()), 0
while True:
    time = pg.time.get_ticks()
    mouse = pg.mouse.get_pos()
    screen.fill((182, 57, 17))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    degree += 1
    mercedes_class.update(degree)
    ellipse.draw(screen)
    pg.display.update()
    clock.tick(30)

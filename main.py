# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pygame as pg
from pygame.locals import *

pg.init()
DISPLAYSURF = pg.display.set_mode((300,300), pg.RESIZABLE)

DISPLAYSURF.fill((0, 0, 0))

pg.display.set_caption("Ändra det här. Line 9 main.py")


FPS = 60
FramesPerTick = pg.time.Clock()


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("textures/gubbe.png")
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)


    def move(self):
        pressed_keys = pg.key.get_pressed()
        if pressed_keys[K_w] and self.rect.top < DISPLAYSURF.get_height()/2:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_s] and self.rect.top > 0-DISPLAYSURF.get_height()/2:
            self.rect.move_ip(0, -3)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()


while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
    P1.move()
    P1.draw(DISPLAYSURF)
    pg.display.update()
    FramesPerTick.tick(FPS)
import math
import pygame as pg

WIDTH = 700 # ширина
HEIGHT = 700 # высота
FPS = 120

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Maxvell")
clock = pg.time.Clock()

running = True

while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()

pg.quit()

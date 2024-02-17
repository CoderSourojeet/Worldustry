import pygame as pg, math
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.pos = PLAYER_START_POS
        self.speed = PLAYER_SPEED

        self.image = pg.transform.rotozoom(pg.image.load('res/entity.png').convert_alpha(), 0, 0.05)
        self.base_image = self.image
        self.hitbox_rect = self.base_image.get_rect(center=self.pos)
        self.rect = self.hitbox_rect.copy()

    def handle_events(self):
        self.velocity = pg.math.Vector2(0, 0)
        
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.velocity.y = -1
        if keys[pg.K_s]:
            self.velocity.y = 1
        if keys[pg.K_a]:
            self.velocity.x = -1
        if keys[pg.K_d]:
            self.velocity.x = 1

        if self.velocity.magnitude() > 0:
            self.velocity = self.velocity.normalize() * PLAYER_SPEED

    def move(self):
        self.pos += self.velocity * self.app.delta_time/60
        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center

    def rotate(self):
        self.mouse_coords = pg.mouse.get_pos()
        self.change_mouse_x = (self.mouse_coords[0] - self.hitbox_rect.centerx)
        self.change_mouse_y = (self.mouse_coords[1] - self.hitbox_rect.centery)
        self.angle = math.degrees(math.atan2(self.change_mouse_y, self.change_mouse_x))
        self.image = pg.transform.rotate(self.base_image, -self.angle)
        self.rect = self.image.get_rect(center=self.hitbox_rect.center)

    def update(self):
        self.handle_events()
        self.move()
        self.rotate()
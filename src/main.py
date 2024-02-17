import pygame as pg, sys
from settings import *
from debug import debug
from player import Player

class Worldustry:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(SCREEN_SIZE, pg.RESIZABLE)
        pg.display.set_caption('Worldustry ' + f'{VERSION}')
        
        self.clock = pg.time.Clock()
        self.delta_time = 0

        self.background = pg.transform.scale(pg.image.load('res/background.png').convert(), SCREEN_SIZE)
        self.player = Player(self)

        self.is_running = True

    def update(self):
        self.player.update()
        self.delta_time = self.clock.tick(FPS)
        
    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player.image, self.player.rect)

        if DEBUG:
            pg.draw.rect(self.screen, 'Red', self.player.rect, width=2)
            pg.draw.rect(self.screen, 'Yellow', self.player.hitbox_rect, width=2)

        pg.display.update()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    app = Worldustry()
    app.run()
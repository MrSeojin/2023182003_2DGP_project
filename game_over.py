from pico2d import *

import game_framework
import play_mode
import title_mode


class Score:
    def __init__(self):
        self.image = load_image("game_over_frame.png")
        self.hand = load_image("click.png")
        self.font = load_font('packdahyun.ttf', 40)
        self.x = 500

    def draw(self):
        self.image.draw(600, 300)
        self.hand.draw(self.x, 100)
        self.font.draw(700, 390, f'{play_mode.gold}',(200,180,50))
        self.font.draw(700, 360, f'{int(play_mode.distance)}',(120,180,255))
        self.font.draw(640, 230, f'{int(play_mode.distance) + play_mode.score * 10 + play_mode.gold}',(120,180,255))

    def update(self):
        pass

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            self.x = 500
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            self.x = 855
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if self.x < 700:
                game_framework.change_mode(play_mode)
            else:
                game_framework.change_mode(title_mode)

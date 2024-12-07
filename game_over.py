from pico2d import load_image, load_font

import play_mode


class Score:
    def __init__(self):
        self.image = load_image('game_over_frame.png')
        self.font = load_font('packdahyun.ttf', 40)

    def draw(self):
        self.image.draw(600, 300)
        self.font.draw(700, 390, f'{play_mode.gold}',(200,180,50))
        self.font.draw(700, 360, f'{int(play_mode.distance)}',(120,180,255))
        self.font.draw(640, 230, f'{int(play_mode.distance) + play_mode.score * 10 + play_mode.gold}',(120,180,255))

    def update(self):
        pass
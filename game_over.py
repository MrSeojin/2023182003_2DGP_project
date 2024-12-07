from pico2d import load_image, load_font

import play_mode


class Score:
    def __init__(self):
        self.image = load_image('game_over_frame.png')
        self.font = load_font('packdahyun.ttf', 40)

    def draw(self):
        self.image.draw(600, 300)
        self.font.draw(640, 230, f'{int(play_mode.score)}',(0,0,5))

    def update(self):
        pass
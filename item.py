from pico2d import*
import game_framework

import game_world

# princess Run Speed
PIXEL_PER_METER = (700.0 / 4.0)  # 10 pixel 10 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class FlyItem:
    def __init__(self):
        self.x = 1300
        self.image = load_image('item_fly.png')

    def update(self):
        self.x -= RUN_SPEED_PPS * game_framework.frame_time

    def get_bb(self):
        return int(self.x) - 50, 300, int(self.x) + 50, 400

    def draw(self):
        self.image.clip_draw(0, 0, 214, 226, int(self.x), 350, 100, 100)
        draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'princess:fly_item':
            game_world.remove_object(self)

class DoubleItem:
    def __init__(self):
        self.x = 1300
        self.image = load_image('item_double.png')

    def update(self):
        self.x -= RUN_SPEED_PPS * game_framework.frame_time

    def get_bb(self):
        return int(self.x) - 50, 300, int(self.x) + 50, 400

    def draw(self):
        self.image.clip_draw(0, 0, 135, 163, int(self.x), 350, 100, 100)
        draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'princess:double_item':
            game_world.remove_object(self)

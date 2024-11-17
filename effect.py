from pico2d import *
import game_world
import game_framework

# princess Run Speed
PIXEL_PER_METER = (4.0 / 0.1)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class SmallEffect:

    def __init__(self, x = 400, y = 300):
        self.x, self.y, self.size = x, y, 0
        self.image = load_image('effect_snow.png')

    def draw(self):
        self.image.clip_draw(0, 0, 200, 181, self.x, self.y, 20 * self.size, 10 * self.size)

    def update(self):
        self.x += 5 * RUN_SPEED_PPS * game_framework.frame_time
        if self.size < 20:
            self.size += RUN_SPEED_PPS * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)


class BigEffect:
    def __init__(self, x = 400, y = 300):
        self.x, self.y, self.size = x, y, 0
        self.image = load_image('effect_snow.png')

    def draw(self):
        self.image.clip_draw(0, 0, 200, 181, self.x, self.y, 20 * self.size, 10 * self.size)

    def update(self):
        self.x += 10 * RUN_SPEED_PPS * game_framework.frame_time
        if self.y > 160:
            self.y -= 5 * RUN_SPEED_PPS * game_framework.frame_time
        if self.y < 160:
            self.y = 160
        if self.size < 20:
            self.size += RUN_SPEED_PPS * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

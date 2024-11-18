from pico2d import *
import game_world
import game_framework

# princess Run Speed
PIXEL_PER_METER = (4.0 / 0.2)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class SmallEffect:

    def __init__(self, x = 400, y = 300):
        self.x, self.y, self.size = x + 150, y, 18
        self.image = load_image('effect_snow.png')

    def get_bb(self):
        return self.x - 10 * self.size, 0, self.x + 10 * self.size, self.y + 20 * self.size

    def draw(self):
        self.image.clip_composite_draw(0, 0, 200, 181, 0, 'h', self.x, self.y, 20 * int(self.size), 10 * int(self.size))
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.x += 5 * RUN_SPEED_PPS * game_framework.frame_time

        self.size -= RUN_SPEED_PPS * game_framework.frame_time / 2
        if self.size < 0:
            self.size = 0
            game_world.remove_object(self)

    def handle_collision(self, group, other):
        if group == 'mob:effect':
            pass


class BigEffect:
    def __init__(self, x = 400, y = 300):
        self.x, self.y, self.size = x + 200, y, 20
        self.image = load_image('effect_snow.png')

    def get_bb(self):
        return self.x - 10 * self.size, 0, self.x + 10 * self.size, 600

    def draw(self):
        self.image.clip_composite_draw(0, 0, 200, 181, 0, 'h', self.x, self.y, 20 * int(self.size), 10 * int(self.size))
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += 5 * RUN_SPEED_PPS * game_framework.frame_time
        if self.y > 160:
            self.y -= 5 * RUN_SPEED_PPS * game_framework.frame_time
        if self.y < 160:
            self.y = 160

        self.size -= RUN_SPEED_PPS * game_framework.frame_time / 2
        if self.size < 0:
            self.size = 0
            game_world.remove_object(self)

    def handle_collision(self, group, other):
        if group == 'mob:effect':
            pass
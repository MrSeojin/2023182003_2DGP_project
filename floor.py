from pico2d import*
import game_framework
import random

import game_world
from mob import Mob

# princess Run Speed
PIXEL_PER_METER = (500.0 / 5)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Floor:
    def __init__(self, x = 0, size = 0, hole = 0):
        self.x = x - hole
        self.size = size
        self.image = load_image('grass.png')

    def update(self):
        self.x += RUN_SPEED_PPS * game_framework.frame_time

        if int(self.x) > self.size + 2000:
            game_world.remove_object(self)

        if 0 <= self.x - self.size <= RUN_SPEED_PPS * game_framework.frame_time:
            now_size = random.randint(600, 1200)
            now_hole = random.randint(0, 400)
            floor = Floor(self.x - self.size, now_size, now_hole)
            game_world.add_object(floor, 1)
            mob = Mob(random.randint(self.size + 2000 - int(self.x), self.size + now_size + 2000 - int(self.x)))
            game_world.add_object(mob, 2)
            if 100 <= now_size or now_hole == 0:
                mob = Mob(random.randint(self.size + 2000 - int(self.x), self.size + now_size + 2000 - int(self.x)))
                game_world.add_object(mob, 2)

    def draw(self):
        self.image.clip_draw(0, 0, self.size, 60, self.size / 2 + 2000 - int(self.x), 40)

    def handle_collision(self, group, other):
        pass

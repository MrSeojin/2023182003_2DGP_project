from pico2d import*
import game_framework
import random

import game_world
import play_mode
from mob import Mob

# princess Run Speed
PIXEL_PER_METER = (700.0 / 4.0)  # 10 pixel 10 cm
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
        if play_mode.princess.action >= 5:
            self.x += 2 * RUN_SPEED_PPS * game_framework.frame_time
        else:
            self.x += RUN_SPEED_PPS * game_framework.frame_time

        if self.x > self.size + 2000:
            game_world.remove_object(self)

        if 0 <= self.x - self.size <= RUN_SPEED_PPS * game_framework.frame_time and play_mode.princess.action < 5:
            now_size = random.randint(100, 1200)
            now_hole = random.randint(0, 800)
            floor = Floor(self.x - self.size, now_size, now_hole)
            game_world.add_collision_pair('princess:floor', None, floor)
            game_world.add_collision_pair('mob:floor', None, floor)
            game_world.add_object(floor, 1)
            if play_mode.fever_time == False and (500 <= now_size or now_hole == 0):
                mob = Mob(random.randint(self.size + now_hole + 2000 - int(self.x), self.size + now_hole + now_size + 2000 - int(self.x)))
                game_world.add_object(mob, 2)
                game_world.add_collision_pair('princess:mob', None, mob)
                game_world.add_collision_pair('mob:effect', mob, None)
                game_world.add_collision_pair('mob:floor', mob, None)
            if play_mode.fever_time == False and (800 <= now_size or now_hole == 0):
                mob = Mob(random.randint(self.size + now_hole + 2000 - int(self.x), self.size + now_hole + now_size + 2000 - int(self.x)))
                game_world.add_object(mob, 2)
                game_world.add_collision_pair('princess:mob', None, mob)
                game_world.add_collision_pair('mob:effect', mob, None)
                game_world.add_collision_pair('mob:floor', mob, None)
        elif 0 <= self.x - self.size <= 2 * RUN_SPEED_PPS * game_framework.frame_time and play_mode.princess.action >= 5:
            now_size = random.randint(100, 1200)
            now_hole = random.randint(0, 800)
            floor = Floor(self.x - self.size, now_size, now_hole)
            game_world.add_collision_pair('princess:floor', None, floor)
            game_world.add_collision_pair('mob:floor', None, floor)
            game_world.add_object(floor, 1)
            if play_mode.fever_time == False and (500 <= now_size or now_hole == 0):
                mob = Mob(random.randint(self.size + now_hole + 2000 - int(self.x),
                                         self.size + now_hole + now_size + 2000 - int(self.x)))
                game_world.add_object(mob, 2)
                game_world.add_collision_pair('princess:mob', None, mob)
                game_world.add_collision_pair('mob:effect', mob, None)
                game_world.add_collision_pair('mob:floor', mob, None)
            if play_mode.fever_time == False and (800 <= now_size or now_hole == 0):
                mob = Mob(random.randint(self.size + now_hole + 2000 - int(self.x),
                                         self.size + now_hole + now_size + 2000 - int(self.x)))
                game_world.add_object(mob, 2)
                game_world.add_collision_pair('princess:mob', None, mob)
                game_world.add_collision_pair('mob:effect', mob, None)
                game_world.add_collision_pair('mob:floor', mob, None)

    def get_bb(self):
        return 2000 - int(self.x), 40, self.size + 2000 - int(self.x), 85

    def draw(self):
        self.image.clip_draw(0, 0, self.size, 60, self.size / 2 + 2000 - int(self.x), 40)
        draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'mob:floor':
            pass
        elif group == 'princess:floor':
            pass

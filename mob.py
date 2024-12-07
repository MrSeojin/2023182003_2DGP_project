from pico2d import*
import random

import game_framework
import game_world
import play_mode
from gold import Gold
from item import FlyItem
from state_machine import*

# mob Run Speed
PIXEL_PER_METER = (35.0 / 0.2)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# ,ob Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Idle:
    @staticmethod
    def enter(mob, e):
        mob.frame, mob.action = 0, 0

    @staticmethod
    def exit(mob, e):
        pass

    @staticmethod
    def do(mob):
        mob.x -= 2 * RUN_SPEED_PPS * game_framework.frame_time
        mob.frame += FRAMES_PER_ACTION * ACTION_PER_TIME*game_framework.frame_time
        if mob.x < 700 and mob.dir != 0:
            mob.state_machine.add_event(('JUMP', 0))
        elif mob.fall:
            mob.state_machine.add_event(('FALL', 0))
        elif mob.type == 0:
            mob.frame %= 3
        elif mob.type != 0:
            mob.frame %= 2

    @staticmethod
    def draw(mob):

        if mob.type == 0:
            mob.image.clip_draw(int(mob.frame) * 70, mob.action * 85, 70, 85, mob.x, mob.y + 85 / 2)
        else:
            mob.image.clip_draw(int(mob.frame) * 65, mob.action * 65, 65, 65, mob.x, mob.y + 65 / 2)

class Move:
    @staticmethod
    def enter(mob, e):
        mob.frame, mob.action = 0, 1

    @staticmethod
    def exit(mob, e):
        pass

    @staticmethod
    def do(mob):
        if mob.dir < 0:
            mob.x += mob.dir * RUN_SPEED_PPS * game_framework.frame_time
        mob.x += 2  * mob.dir * RUN_SPEED_PPS * game_framework.frame_time
        if mob.type == 0:
            mob.frame = (mob.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 7
        else:
            mob.frame = (mob.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 3
        if mob.fall:
            mob.state_machine.add_event(('FALL', 0))

    @staticmethod
    def draw(mob):
        if mob.type == 0:
            if mob.dir < 0:
                mob.image.clip_draw(int(mob.frame) * 70, mob.action * 85, 70, 85, mob.x, mob.y + 85 / 2)
            else:
                mob.image.clip_composite_draw(int(mob.frame) * 70, mob.action * 85, 70, 85, 0, 'h', mob.x, mob.y + 85 / 2, 70, 85)
        else:
            if mob.dir < 0:
                mob.image.clip_draw(int(mob.frame) * 65, mob.action * 65, 65, 65, mob.x, mob.y + 65 / 2)
            else:
                mob.image.clip_composite_draw(int(mob.frame) * 65, mob.action * 65, 65, 65, 0, 'h', mob.x, mob.y + 65 / 2, 65, 65)

class Jump:
    @staticmethod
    def enter(mob, e):
        mob.y += 10
        mob.frame, mob.action = 0, 2

    @staticmethod
    def exit(mob, e):
        mob.y -= 10

    @staticmethod
    def do(mob):
        mob.x -= 2 * RUN_SPEED_PPS * game_framework.frame_time
        mob.frame += FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
        if mob.frame >= 1:
            mob.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(mob):
        if mob.type == 0:
            mob.image.clip_draw(int(mob.frame) * 70, mob.action * 85, 70, 85, mob.x, mob.y + 85 / 2)
        else:
            mob.image.clip_draw(int(mob.frame)* 65, mob.action * 65, 65, 65, mob.x, mob.y + 65 / 2)

class Hit:
    @staticmethod
    def enter(mob, e):
        if random.randint(0,10) == 1:
            item = FlyItem()
            game_world.add_object(item, 1)
            game_world.add_collision_pair('princess:fly_item', None, item)
        else:
            coin = Gold(mob.x + 100)
            game_world.add_object(coin, 1)
            game_world.add_collision_pair('princess:gold', None, coin)
        mob.frame, mob.action = 0, 3

    @staticmethod
    def exit(mob, e):
        pass

    @staticmethod
    def do(mob):
        mob.frame += FRAMES_PER_ACTION*ACTION_PER_TIME * game_framework.frame_time

        if mob.frame > 1:
            if mob.fall:
                mob.state_machine.add_event(('FALL', 0))
            else:
                mob.state_machine.add_event(('DEATH', 0))

    @staticmethod
    def draw(mob):
        if mob.type == 0:
            mob.image.clip_draw(0, mob.action * 85, 70, 85, mob.x, mob.y + 85 / 2)
        else:
            mob.image.clip_draw(0, mob.action * 65, 65, 65, mob.x, mob.y + 65 / 2)

class Die:
    @staticmethod
    def enter(mob, e):
        mob.frame, mob.action = 0, 4

    @staticmethod
    def exit(mob, e):
        game_world.remove_object(mob)

    @staticmethod
    def do(mob):
        mob.x -= 2 * RUN_SPEED_PPS * game_framework.frame_time
        mob.frame += FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
        if mob.type == 0 and mob.frame >= 4:
            mob.state_machine.add_event(('DEATH', 0))
        elif mob.type !=0 and mob.frame >= 3:
            mob.state_machine.add_event(('DEATH', 0))

    @staticmethod
    def draw(mob):
        if mob.type == 0:
            mob.image.clip_draw(int(mob.frame) * 70, mob.action * 85, 70, 85, mob.x, mob.y + 40)
        else:
            mob.image.clip_draw(int(mob.frame) * 65, mob.action * 65, 65, 65, mob.x, mob.y + 30)

class Fall:
    @staticmethod
    def enter(mob, e):
        if mob.action == 2:
            mob.action = 1

    @staticmethod
    def exit(mob, e):
        pass

    @staticmethod
    def do(mob):
        if mob.dir < 0:
            mob.x += mob.dir * RUN_SPEED_PPS * game_framework.frame_time
        mob.frame = FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        mob.y -= RUN_SPEED_PPS * game_framework.frame_time
        if mob.action == 0:
            if mob.type == 0:
                mob.frame %= 3
            elif mob.type != 0:
                mob.frame %= 2
        elif mob.action == 1:
            if mob.type == 0:
                mob.frame %= 7
            elif mob.type != 0:
                mob.frame %= 3
        else:
            mob.frame = 0

    @staticmethod
    def draw(mob):
        if mob.type == 0:
            mob.image.clip_draw(int(mob.frame) * 70, mob.action * 85, 70, 85, mob.x, mob.y + 40)
        else:
            mob.image.clip_draw(int(mob.frame) * 65, mob.action * 65, 65, 65, mob.x, mob.y + 30)

class Mob:
    hit_sound = None
    def __init__(self, x = 1250):
        self.delay = 0
        self.x, self.y = x, 60
        self.frame, self.action = 0, 0
        self.dir = random.randint(-1,1)
        self.type = random.randint(0, 2)
        self.fall = False
        if self.type == 0:
            self.image = load_image('mob_slime_animation_sheet.png')
        elif self.type == 1:
            self.image = load_image('mob_blue_animation_sheet.png')
        else:
            self.image = load_image('mob_spots_animation_sheet.png')
        Mob.hit_sound = load_wav('mob_damage_sound.wav')
        Mob.hit_sound.set_volume(32)
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle : {time_out : Move, jump : Jump, hit_object: Hit, fall : Fall},
                Move : {time_out : Jump, hit_object: Hit, fall : Fall},
                Jump : {time_out : Move, hit_object: Hit, fall : Fall},
                Hit : {death : Die, hit_object: Hit, fall : Fall},
                Fall : {death : Die},
                Die : {death : Die}
            }
        )
    def update(self):
        if play_mode.princess.stop:
            self.y += RUN_SPEED_PPS * game_framework.frame_time / 2 * self.dir
            if self.y <= 60:
                self.y = 60
                self.dir = 1
            elif self.y > 100:
                self.dir = -1
        else:
            self.delay += 1
            if self.delay % 2:
                self.state_machine.update()
        self.fall = True

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def get_bb(self):
        if self.type == 0:
            return self.x - 35, self.y, self.x + 35, self.y + 70
        else:
            return self.x - 32.5, self.y, self.x + 32.5, self.y + 65

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'princess:mob':
            pass
        if group == 'mob:effect':
            Mob.hit_sound.play()
            game_world.remove_collision_object(self)
            game_world.add_collision_pair('mob:floor', self, None)
            self.state_machine.add_event(('HIT', 0))
        if group == 'mob:floor':
            self.fall = False

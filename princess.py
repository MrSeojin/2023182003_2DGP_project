from pico2d import*

import game_framework
import game_world
from effect import SmallEffect, BigEffect
from state_machine import*

# princess Run Speed
PIXEL_PER_METER = (10.0 / 0.2)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# princess Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 16

class Run:
    @staticmethod
    def enter(princess, e):
        princess.action = 0
        if time_out(e):
            pass
        else:
            princess.frame = 0

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        princess.frame = (princess.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 16
        if princess.y > 60:
            princess.y -= RUN_SPEED_PPS * game_framework.frame_time
        if princess.y < 60:
            princess.y = 60

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class Hit:
    @staticmethod
    def enter(princess, e):
        princess.frame, princess.action = 0, 2
        princess.count = 0

        effect = SmallEffect(princess.x, princess.y + 100)
        game_world.add_object(effect, 3)
        game_world.add_collision_pair('mob:effect', None, effect)

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        princess.frame +=  FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
        if princess.frame >= 10:
            princess.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class BigHit:
    @staticmethod
    def enter(princess, e):
        princess.frame, princess.action = 10, 2
        princess.count = 0

        effect = BigEffect(princess.x, princess.y + 100)
        game_world.add_object(effect, 3)
        game_world.add_collision_pair('mob:effect', None, effect)

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        if princess.action == 2:
            princess.frame += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
            if princess.frame >= 16:
                princess.action = 0
                princess.frame = 10
            princess.y -= RUN_SPEED_PPS * game_framework.frame_time
        else:
            princess.frame = (princess.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 16
            princess.y -= 2 * RUN_SPEED_PPS * game_framework.frame_time
        if princess.y < 60:
            princess.y = 60
        if princess.y == 60:
            princess.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class Jump:
    @staticmethod
    def enter(princess, e):
        princess.action = 1
        if time_out(e):
            princess.frame = 6
        else:
            princess.frame = 0

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        if princess.action == 1:
            princess.frame += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
            if princess.frame <= 8:
                princess.y += 3 * RUN_SPEED_PPS * game_framework.frame_time
            else:
                princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time
            if princess.frame >= 12:
                princess.action = 0
                princess.frame = 10
        else:
            princess.frame = (princess.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 16
            princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time
        if princess.y < 60:
                princess.y = 60
        if princess.y == 60:
            princess.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class DoubleJump:
    @staticmethod
    def enter(princess, e):
        princess.frame, princess.action = 0, 3

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        if princess.action == 3:
            princess.frame += FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
            princess.y += 3 * RUN_SPEED_PPS * game_framework.frame_time
            if princess.frame >= 6:
                princess.action = 1
                princess.frame = 5
        elif princess.action == 1:
            princess.frame += FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
            princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time
            if princess.frame >= 12:
                princess.action = 0
                princess.frame = 10
        else:
            princess.frame = (princess.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 16
            princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time
        if princess.y < 60:
            princess.y = 60
        if princess.y == 60:
            princess.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class Fly:
    @staticmethod
    def enter(princess, e):
        pass

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        pass

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class Die:
    @staticmethod
    def enter(princess, e):
        pass

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        pass

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class Fall:
    @staticmethod
    def enter(princess, e):
        princess.action = 0

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        princess.frame = (princess.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 16
        princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time
        if princess.y < 0:
            princess.state_machine.add_event(('DEATH', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class Princess:
    def __init__(self):
        self.x, self.y = 300, 60

        self.frame, self.action = 0, 0
        self.image = load_image('princess_snow_animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Run)
        self.state_machine.set_transitions(
            {
                Run : {c_down : Hit, space_down : Jump, death : Die, fall : Fall},
                Hit : {time_out : Run, space_down : Jump, death : Die},
                BigHit : {time_out : Run, fly_item : Fly, death : Die, fall : Fall},
                Jump : {c_down : BigHit, space_down : DoubleJump,  time_out : Run, fly_item : Fly, death : Die, fall : Fall},
                DoubleJump : {c_down : BigHit, time_out : Run, fly_item : Fly, death : Die, fall : Fall},
                Fly : {time_out : Run},
                Fall : {death : Die}
            }
        )
    def update(self):
        self.state_machine.update()

    def get_bb(self):
        return self.x - 100, self.y + 20, self.x - 10, self.y + 170

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'princess:mob':
            pass
        if group == 'princess:gold':
            pass
            #self.state_machine.add_event(('FALL', 0))

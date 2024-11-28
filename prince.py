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
    def enter(prince, e):
        prince.action = 0
        if time_out(e):
            pass
        else:
            prince.frame = 0

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(prince):
        prince.frame = (prince.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 8

    @staticmethod
    def draw(prince):
        prince.image.clip_draw(int(prince.frame) * 200, prince.action * 200, 200, 200, int(prince.x), int(prince.y) + 100)

class Fall:
    @staticmethod
    def enter(prince, e):
        prince.action = 0

    @staticmethod
    def exit(prince, e):
        pass

    @staticmethod
    def do(prince):
        pass

    @staticmethod
    def draw(prince):
        prince.image.clip_draw(int(prince.frame) * 200, prince.action * 200, 200, 200, int(prince.x), int(prince.y) + 135)

class Prince:
    def __init__(self):
        self.x, self.y = 400, 60

        self.frame, self.action = 0, 0
        self.image = load_image('prince_animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Run)
        self.state_machine.set_transitions(
            {
                Run : {},
                Fall : {}
            }
        )
    def update(self):
        self.state_machine.update()

    def get_bb(self):
        return self.x - 100, self.y, self.x + 100, self.y + 185

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass

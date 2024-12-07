from pico2d import*

import game_framework
import game_world
from state_machine import*
import play_mode

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
        if play_mode.fever_time == False:
            prince.state_machine.add_event(('TIME_OUT', 0))
        prince.x -= RUN_SPEED_PPS * game_framework.frame_time
        prince.y -= RUN_SPEED_PPS * game_framework.frame_time
        if prince.y < 60:
            prince.y = 60
        if prince.x < 400:
            prince.x = 400

    @staticmethod
    def draw(prince):
        prince.image.clip_draw(int(prince.frame) * 200, prince.action * 200, 200, 200, int(prince.x), int(prince.y) + 95)

class GoAway:
    @staticmethod
    def enter(prince, e):
        prince.action = 0

    @staticmethod
    def exit(prince, e):
        pass

    @staticmethod
    def do(prince):
        prince.frame = (prince.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 8
        prince.x += RUN_SPEED_PPS * game_framework.frame_time
        prince.y -= RUN_SPEED_PPS * game_framework.frame_time
        if prince.y < 60:
            prince.y = 60
        if prince.x > 1300:
            game_world.remove_object(prince)

    @staticmethod
    def draw(prince):
        prince.image.clip_draw(int(prince.frame) * 200, prince.action * 200, 200, 200, int(prince.x), int(prince.y) + 95)

class Prince:
    hit_sound = None
    def __init__(self):
        self.x, self.y = 400, 60

        self.frame, self.action = 0, 0
        self.image = load_image('prince_animation_sheet.png')
        Prince.hit_sound = load_wav('prince_damage_sound.wav')
        Prince.hit_sound.set_volume(32)

        self.state_machine = StateMachine(self)
        self.state_machine.start(Run)
        self.state_machine.set_transitions(
            {
                Run : {time_out : GoAway},
                GoAway : {time_out : GoAway}
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
        if group == 'prince:effect':
            if play_mode.sound_play == 'play':
                Prince.hit_sound.play()
            self.x += 20
            self.y += 20
            play_mode.score += 5

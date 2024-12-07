from pico2d import*

import game_framework
import game_world
import play_mode
from back_ground import Fever
from effect import SmallEffect, BigEffect
from prince import Prince
from game_over import Score
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
        princess.frame = (princess.frame + FRAMES_PER_ACTION*ACTION_PER_TIME * game_framework.frame_time) % 16
        if princess.y > 60:
            princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time
        if princess.y <= 60:
            princess.jump_num = 0
            princess.y = 60

        if princess.fall and princess.y <= 60:
           princess.state_machine.add_event(('FALL', 0))

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
        game_world.add_collision_pair('prince:effect', None, effect)


    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        princess.frame +=  FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
        if princess.frame >= 10:
            princess.jump_num = 0
            princess.state_machine.add_event(('TIME_OUT', 0))

        if princess.fall:
           princess.state_machine.add_event(('FALL', 0))

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
        game_world.add_collision_pair('prince:effect', None, effect)

    @staticmethod
    def exit(princess, e):
        if 60 - RUN_SPEED_PPS * game_framework.frame_time <= princess.y <= 60:
            princess.y = 60

    @staticmethod
    def do(princess):
        princess.frame += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        if princess.frame >= 16:
            princess.frame = 10
            if 60 - 3 * RUN_SPEED_PPS * game_framework.frame_time <= princess.y <= 60:
                princess.y = 60
            if princess.y < 60:
                princess.state_machine.add_event(('FALL', 0))
            else:
                princess.state_machine.add_event(('TIME_OUT', 0))
        princess.y -= RUN_SPEED_PPS * game_framework.frame_time

        if 60 - 3 * RUN_SPEED_PPS * game_framework.frame_time <= princess.y <= 60:
            princess.y = 60
        if princess.y <= 60:
            if princess.y < 60:
                princess.state_machine.add_event(('FALL', 0))
            else:
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
            if play_mode.quest.type == 1:
                play_mode.quest.num += 1
            princess.frame = 0
            princess.jump_num += 1
            if princess.jump_num <= 2:
                Princess.jump_sound.play()

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        if princess.jump_num > 2:
            if princess.y >= 60 or princess.fall == False:
                princess.state_machine.add_event(('TIME_OUT', 0))
            else:
                princess.state_machine.add_event(('FALL', 0))

        if princess.action == 1:
            princess.frame += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
            if princess.frame <= 8:
                princess.y += 3 * RUN_SPEED_PPS * game_framework.frame_time
            else:
                princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time

                if princess.action != 3 and 60 - 3 * RUN_SPEED_PPS * game_framework.frame_time <= princess.y <= 60:
                    princess.y = 60
                if princess.action != 3 and princess.y <= 60:
                    if princess.fall and princess.y <= 60:
                        princess.state_machine.add_event(('FALL', 0))
                    else:
                        princess.jump_num = 0
                        princess.state_machine.add_event(('TIME_OUT', 0))
            if princess.frame >= 12:
                princess.action = 0
                princess.frame = 10
        else:
            princess.frame = (princess.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 16
            princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time

            if princess.action != 3 and 60 - 3 * RUN_SPEED_PPS * game_framework.frame_time <= princess.y <= 60:
                princess.y = 60
            if princess.action != 3 and princess.y <= 60:
                if princess.fall and princess.y <= 60:
                    princess.state_machine.add_event(('FALL', 0))
                else:
                    princess.jump_num = 0
                    princess.state_machine.add_event(('TIME_OUT', 0))



    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class DoubleJump:
    @staticmethod
    def enter(princess, e):
        if time_out(e):
            princess.frame, princess.action = 0, 1
        else:
            if play_mode.quest.type == 2:
                play_mode.quest.num += 1
            princess.frame, princess.action = 0, 3
            princess.jump_num += 1
            if princess.jump_num <= 2:
                Princess.jump_sound.play()

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        if princess.jump_num > 2:
            if princess.y >= 60 or princess.fall == False:
                princess.state_machine.add_event(('TIME_OUT', 0))
            else:
                princess.state_machine.add_event(('FALL', 0))

        else:
            if princess.action == 3:
                princess.frame += FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
                princess.y += 3 * RUN_SPEED_PPS * game_framework.frame_time
                if princess.frame >= 6:
                    princess.action = 1
                    princess.frame = 5
            elif princess.action == 1:
                princess.frame += FRAMES_PER_ACTION*ACTION_PER_TIME * game_framework.frame_time
                princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time

                if princess.action != 3 and 60 - 3 * RUN_SPEED_PPS * game_framework.frame_time <= princess.y <= 60:
                    princess.y = 60
                if princess.action != 3 and princess.y <= 60:
                    if princess.fall and princess.y <= 60:
                        princess.state_machine.add_event(('FALL', 0))
                    else:
                        princess.jump_num = 0
                        princess.state_machine.add_event(('TIME_OUT', 0))

                if princess.frame >= 12:
                    princess.action = 0
                    princess.frame = 10
            else:
                princess.frame = (princess.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 16
                princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time

                if princess.action != 3 and 60 - 3 * RUN_SPEED_PPS * game_framework.frame_time <= princess.y <= 60:
                    princess.y = 60
                if princess.action != 3 and princess.y <= 60:
                    if princess.fall and princess.y <= 60:
                        princess.state_machine.add_event(('FALL', 0))
                    else:
                        princess.jump_num = 0
                        princess.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class Fly:
    @staticmethod
    def enter(princess, e):
        princess.action = 5
        princess.frame = 0
        if play_mode.fever_time:
            pass

    @staticmethod
    def exit(princess, e):
        princess.frame = 0

    @staticmethod
    def do(princess):
        if princess.action == 5:
            princess.y += 3 * RUN_SPEED_PPS * game_framework.frame_time
            princess.x += RUN_SPEED_PPS * game_framework.frame_time
            if princess.y >= 300:
                princess.action = 6
                if play_mode.fever_time:
                    fever = Fever()
                    game_world.add_object(fever, 0)
        elif princess.action == 6:
            princess.frame += FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
            princess.x += 5 * RUN_SPEED_PPS * game_framework.frame_time
            if princess.x > 500:
                princess.x = 500
            if princess.frame >= 80:
                princess.action = 0
        elif princess.action == 0:
            princess.y -= 3 * RUN_SPEED_PPS * game_framework.frame_time
            princess.x -= 5 * RUN_SPEED_PPS * game_framework.frame_time
            if princess.x < 300:
                princess.x = 300
            if princess.y <= 60:
                princess.y = 60
            if princess.y == 60:
                princess.x = 300
                if play_mode.fever_time:
                    prince = Prince()
                    game_world.add_object(prince, 2)
                    game_world.add_collision_pair('prince:effect', prince, None)
                princess.jump_num = 0
                princess.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(princess):
        princess.fly_image.clip_draw(0, 0, 374, 381, int(princess.x), int(princess.y) + 135)


class Die:
    @staticmethod
    def enter(princess, e):
        princess.action, princess.frame = 3, 10

    @staticmethod
    def exit(princess, e):
        princess.stop = True
        total_score = Score()
        game_world.add_object(total_score, 3)


    @staticmethod
    def do(princess):
        if princess.stop:
            pass
        else:
            princess.frame += FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time / 5

            if princess.frame >= 16:
                princess.state_machine.add_event(('TIME_OUT', 0))

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
        if princess.y < -300:
            princess.state_machine.add_event(('DEATH', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(int(princess.frame) * 300, princess.action * 300, 300, 300, int(princess.x), int(princess.y) + 135)

class Princess:
    jump_sound = None
    def __init__(self):
        self.x, self.y = 300, 60
        self.fall = False
        self.jump_num = 0
        Princess.jump_sound = load_wav('princess_jump_sound.wav')
        Princess.jump_sound.set_volume(32)
        self.stop = False

        self.frame, self.action = 0, 0
        self.image = load_image('princess_snow_animation_sheet.png')
        self.fly_image = load_image('princess_snow_fly.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Run)
        self.state_machine.set_transitions(
            {
                Run : {c_down : Hit, space_down : Jump, death : Die, fall : Fall,fly_item : Fly,},
                Hit : {time_out : Run, space_down : Jump, death : Die,fly_item : Fly,},
                BigHit : {time_out : DoubleJump, fly_item : Fly, death : Die, fall : Fall, space_down : Jump},
                Jump : {c_down : BigHit, space_down : DoubleJump,  time_out : Run, fly_item : Fly, death : Die, fall : Fall},
                DoubleJump : {c_down : BigHit, time_out : Run, fly_item : Fly, death : Die, fall : Fall},
                Fly : {time_out : Run, fly_item : Fly,},
                Fall : {death : Die, space_down : Jump, fly_item : Fly,},
                Die : {time_out : Die}
            }
        )
    def update(self):
        self.state_machine.update()
        self.fall = True

    def get_bb(self):
        return self.x - 100, self.y + 20, self.x - 10, self.y + 170

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'princess:floor':
            self.fall = False
        if group == 'princess:mob':
            self.state_machine.add_event(('DEATH', 0))
        if group == 'princess:gold':
            play_mode.gold += 1
        if group == 'princess:fly_item':
            self.state_machine.add_event(('FLY_ITEM', 0))
        if group == 'princess:double_item':
            pass

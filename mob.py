from pico2d import*
import random
from state_machine import*

class Idle:
    @staticmethod
    def enter(mob, e):
        mob.frame, mob.action = 0, 0

    @staticmethod
    def exit(mob, e):
        pass

    @staticmethod
    def do(mob):
        mob.frame += 1
        if mob.type == 0 and mob.frame >= 3 and mob.dir != 0:
            mob.state_machine.add_event(('TIME_OUT', 0))
        elif mob.type == 0:
            mob.frame %= 3
        if mob.type != 0 and mob.frame >= 2 and mob.dir != 0:
            mob.state_machine.add_event(('TIME_OUT', 0))
        elif mob.type != 0:
            mob.frame %= 2

    @staticmethod
    def draw(mob):

        if mob.type == 0:
            mob.image.clip_draw(mob.frame * 70, mob.action * 85, 70, 85, mob.x, mob.y + 85 / 2)
        else:
            mob.image.clip_draw(mob.frame * 65, mob.action * 65, 65, 65, mob.x, mob.y + 65 / 2)

class Move:
    @staticmethod
    def enter(mob, e):
        mob.frame, mob.action = 0, 1

    @staticmethod
    def exit(mob, e):
        pass

    @staticmethod
    def do(mob):
        mob.x += mob.dir
        if mob.type == 0:
            mob.frame = (mob.frame + 1) % 7
        else:
            mob.frame = (mob.frame + 1) % 3

    @staticmethod
    def draw(mob):
        if mob.type == 0:
            if mob.dir < 0:
                mob.image.clip_draw(mob.frame * 70, mob.action * 85, 70, 85, mob.x, mob.y + 85 / 2)
            else:
                mob.image.clip_composite_draw(mob.frame * 70, mob.action * 85, 70, 85, 0, 'h', mob.x, mob.y + 85 / 2, 70, 85)
        else:
            if mob.dir < 0:
                mob.image.clip_draw(mob.frame * 65, mob.action * 65, 65, 65, mob.x, mob.y + 65 / 2)
            else:
                mob.image.clip_composite_draw(mob.frame * 65, mob.action * 65, 65, 65, 0, 'h', mob.x, mob.y + 65 / 2, 65, 65)

class Jump:
    @staticmethod
    def enter(mob, e):
        mob.frame, mob.action = 0, 2

    @staticmethod
    def exit(mob, e):
        pass

    @staticmethod
    def do(mob):
        mob.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(mob):
        if mob.type == 0:
            mob.image.clip_draw(mob.frame * 70, mob.action * 85, 70, 85, mob.x, mob.y + 85 / 2)
        else:
            mob.image.clip_draw(mob.frame * 65, mob.action * 65, 65, 65, mob.x, mob.y + 65 / 2)

class Hit:
    @staticmethod
    def enter(mob, e):
        mob.frame, mob.action = 0, 3

    @staticmethod
    def exit(mob, e):
        pass

    @staticmethod
    def do(mob):
        mob.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(mob):
        if mob.type == 0:
            mob.image.clip_draw(mob.frame * 70, mob.action * 85, 70, 85, mob.x, mob.y + 85 / 2)
        else:
            mob.image.clip_draw(mob.frame * 65, mob.action * 65, 65, 65, mob.x, mob.y + 65 / 2)

class Die:
    @staticmethod
    def enter(mob, e):
        mob.frame, mob.action = 0, 4

    @staticmethod
    def exit(mob, e):
        pass

    @staticmethod
    def do(mob):
        mob.frame += 1
        if mob.type == 0 and mob.frame >= 4:
            mob.state_machine.add_event(('TIME_OUT', 0))
        elif mob.type !=0 and mob.frame >= 3:
            mob.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(mob):
        if mob.type == 0:
            mob.image.clip_draw(mob.frame * 70, mob.action * 85, 70, 85, mob.x, mob.y)
        else:
            mob.image.clip_draw(mob.frame * 65, mob.action * 65, 65, 65, mob.x, mob.y)

class Mob:
    def __init__(self):
        self.delay = 0
        self.x, self.y = 799, 60
        self.frame, self.action = 0, 0
        self.dir = random.randint(-1,1)
        self.type = random.randint(0, 2)
        if self.type == 0:
            self.image = load_image('mob_slime_animation_sheet.png')
            self.hp = 150
        elif self.type == 1:
            self.image = load_image('mob_blue_animation_sheet.png')
            self.hp = 180
        else:
            self.image = load_image('mob_spots_animation_sheet.png')
            self.hp = 200
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle : {time_out : Move},
                Move : {time_out : Jump},
                Jump : {time_out : Jump},
                Hit : {time_out : Die},
                Die : {time_out : Die}
            }
        )
    def update(self):
        self.delay += 1
        if self.delay % 2:
            self.state_machine.update()
    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))
    def draw(self):
        self.state_machine.draw()
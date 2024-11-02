from pico2d import*
from state_machine import*

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
        princess.frame = (princess.frame + 1) % 16
        if princess.y > 150:
            princess.y -= 20
        if princess.y < 150:
            princess.y = 150
    @staticmethod
    def draw(princess):
        princess.image.clip_draw(princess.frame * 300, princess.action * 300, 300, 300, princess.x, princess.y)

class Hit:
    @staticmethod
    def enter(princess, e):
        princess.frame, princess.action = 0, 2
        princess.count = 0

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        princess.frame += 1
        if princess.frame >= 10:
            princess.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(princess.frame * 300, princess.action * 300, 300, 300, princess.x, princess.y)

class BigHit:
    @staticmethod
    def enter(princess, e):
        princess.frame, princess.action = 10, 2
        princess.count = 0

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        if princess.action == 2:
            princess.frame += 1
            if princess.frame >= 16:
                princess.action = 0
                princess.frame = 10
            princess.y -= 10
            if princess.y < 150:
                princess.y = 150
        else:
            princess.frame = (princess.frame + 1) % 16
            princess.y -= 20
            if princess.y < 150:
                princess.y = 150
        if princess.y == 150:
            princess.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(princess.frame * 300, princess.action * 300, 300, 300, princess.x, princess.y)

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
            princess.frame += 1
            if princess.frame <= 6:
                princess.y += 30
            else:
                princess.y -= 30
            if princess.frame >= 12:
                princess.action = 0
                princess.frame = 10
        else:
            princess.frame = (princess.frame + 1) % 16
            princess.y -= 20
            if princess.y < 150:
                princess.y = 150
        if princess.y == 150:
            princess.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(princess.frame * 300, princess.action * 300, 300, 300, princess.x, princess.y)

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
            princess.frame += 1
            princess.y += 30
            if princess.frame >= 6:
                princess.action = 1
                princess.frame = 5
        elif princess.action == 1:
            princess.frame += 1
            princess.y -= 30
            if princess.frame >= 12:
                princess.action = 0
                princess.frame = 10
        else:
            princess.frame = (princess.frame + 1) % 16
            princess.y -= 20
        if princess.y < 150:
            princess.y = 150
        if princess.y == 150:
            princess.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(princess):
        princess.image.clip_draw(princess.frame * 300, princess.action * 300, 300, 300, princess.x, princess.y)

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
        princess.image.clip_draw(princess.frame * 300, princess.action * 300, 300, 300, princess.x, princess.y)

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
        princess.image.clip_draw(princess.frame * 300, princess.action * 300, 300, 300, princess.x, princess.y)

class Princess:
    def __init__(self):
        self.x, self.y = 300, 150
        self.frame, self.action = 0, 0
        self.dir = 0
        self.image = load_image('princess_snow_animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Run)
        self.state_machine.set_transitions(
            {
                Run : {c_down : Hit, space_down : Jump, death : Die},
                Hit : {time_out : Run, death : Die},
                BigHit : {time_out : Run, fly_item : Fly, death : Die},
                Jump : {c_down : BigHit, space_down : DoubleJump,  time_out : Run, fly_item : Fly, death : Die},
                DoubleJump : {c_down : BigHit, time_out : Run, fly_item : Fly, death : Die},
                Fly : {time_out : Run}

            }
        )
    def update(self):
        self.state_machine.update()
    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))
    def draw(self):
        self.state_machine.draw()
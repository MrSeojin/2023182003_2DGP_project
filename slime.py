from pico2d import*
from state_machine import*

class Idle:
    @staticmethod
    def enter(Slime, e):
        pass

    @staticmethod
    def exit(Slime, e):
        pass

    @staticmethod
    def do(Slime):
        pass

    @staticmethod
    def draw(Slime):
        Slime.image.clip_draw(Slime.frame * 70, Slime.action * 85, 70, 85, Slime.x, Slime.y)

class Move:
    @staticmethod
    def enter(Slime, e):
        pass

    @staticmethod
    def exit(Slime, e):
        pass

    @staticmethod
    def do(Slime):
        pass

    @staticmethod
    def draw(Slime):
        Slime.image.clip_draw(Slime.frame * 70, Slime.action * 85, 70, 85, Slime.x, Slime.y)

class Jump:
    @staticmethod
    def enter(Slime, e):
        pass

    @staticmethod
    def exit(Slime, e):
        pass

    @staticmethod
    def do(Slime):
        pass

    @staticmethod
    def draw(Slime):
        Slime.image.clip_draw(Slime.frame * 70, Slime.action * 85, 70, 85, Slime.x, Slime.y)

class Hit:
    @staticmethod
    def enter(Slime, e):
        pass

    @staticmethod
    def exit(Slime, e):
        pass

    @staticmethod
    def do(Slime):
        pass

    @staticmethod
    def draw(Slime):
        Slime.image.clip_draw(Slime.frame * 70, Slime.action * 85, 70, 85, Slime.x, Slime.y)

class Die:
    @staticmethod
    def enter(Slime, e):
        pass

    @staticmethod
    def exit(Slime, e):
        pass

    @staticmethod
    def do(Slime):
        pass

    @staticmethod
    def draw(Slime):
        Slime.image.clip_draw(Slime.frame * 70, Slime.action * 85, 70, 85, Slime.x, Slime.y)

class Slime:
    def __init__(self):
        self.x, self.y = 799, 102
        self.frame, self.action = 0, 0
        self.dir = 0
        self.image = load_image('mob_slime_animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle : {},
                Move : {},
                Jump : {},
                Hit : {},
                Die : {}
            }
        )
    def update(self):
        self.state_machine.update()
    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))
    def draw(self):
        self.state_machine.draw()
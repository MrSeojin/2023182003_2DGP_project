from pico2d import*
from state_machine import*

class Idle:
    @staticmethod
    def enter(Mushroom, e):
        pass

    @staticmethod
    def exit(Mushroom, e):
        pass

    @staticmethod
    def do(Mushroom):
        pass

    @staticmethod
    def draw(Mushroom):
        Mushroom.image.clip_draw(Mushroom.frame * 65, Mushroom.action * 65, 65, 65, Mushroom.x, Mushroom.y)

class Move:
    @staticmethod
    def enter(Mushroom, e):
        pass

    @staticmethod
    def exit(Mushroom, e):
        pass

    @staticmethod
    def do(Mushroom):
        pass

    @staticmethod
    def draw(Mushroom):
        Mushroom.image.clip_draw(Mushroom.frame * 65, Mushroom.action * 65, 65, 65, Mushroom.x, Mushroom.y)

class Jump:
    @staticmethod
    def enter(Mushroom, e):
        pass

    @staticmethod
    def exit(Mushroom, e):
        pass

    @staticmethod
    def do(Mushroom):
        pass

    @staticmethod
    def draw(Mushroom):
        Mushroom.image.clip_draw(Mushroom.frame * 65, Mushroom.action * 65, 65, 65, Mushroom.x, Mushroom.y)

class Hit:
    @staticmethod
    def enter(Mushroom, e):
        pass

    @staticmethod
    def exit(Mushroom, e):
        pass

    @staticmethod
    def do(Mushroom):
        pass

    @staticmethod
    def draw(Mushroom):
        Mushroom.image.clip_draw(Mushroom.frame * 65, Mushroom.action * 65, 65, 65, Mushroom.x, Mushroom.y)

class Die:
    @staticmethod
    def enter(Mushroom, e):
        pass

    @staticmethod
    def exit(Mushroom, e):
        pass

    @staticmethod
    def do(Mushroom):
        pass

    @staticmethod
    def draw(Mushroom):
        Mushroom.image.clip_draw(Mushroom.frame * 65, Mushroom.action * 65, 65, 65, Mushroom.x, Mushroom.y)

class Mushroom:
    def __init__(self):
        self.x, self.y = 799, 100
        self.frame, self.action = 0, 0
        self.dir = 0
        self.image = load_image('mob_blue_animation_sheet.png')
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
from pico2d import*
from state_machine import*

class Run:
    @staticmethod
    def enter(princess, e):
        princess.frame, princess.action = 0, 0

    @staticmethod
    def exit(princess, e):
        pass

    @staticmethod
    def do(princess):
        princess.frame = (princess.frame + 1) % 16
        if princess.y > 150:
            princess.y -= 10
        if princess.y < 150:
            princess.y = 150
    @staticmethod
    def draw(princess):
        princess.image.clip_draw(princess.frame * 100, princess.action * 100, 100, 100, princess.x, princess.y, 200, 200)

class Hit:
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
        pass

class Jump:
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
        pass

class DoubleJump:
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
        pass

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
        pass

class Princess:
    def __init__(self):
        self.x, self.y = 300, 150
        self.frame, self.action = 0, 0
        self.dir = 0
        self.image = load_image('princess_snow_run_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Run)
        self.state_machine.set_transitions(
            {
                Run : {},
                Hit : {},
                Jump : {},
                DoubleJump : {},
                Fly : {}
            }
        )
    def update(self):
        self.state_machine.update()
    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))
    def draw(self):
        self.state_machine.draw()
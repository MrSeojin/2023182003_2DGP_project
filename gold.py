from pico2d import*

import game_framework

# princess Run Speed
PIXEL_PER_METER = (35.0 / 0.2)  # 10 pixel 10 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Gold:
    def __init__(self, x):
        self.x, self.y = x, 350
        self.frame, self.action = 0, 0
        self.image = load_image('coin.png')
    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x -= RUN_SPEED_PPS * game_framework.frame_time

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def draw(self):
        self.image.clip_draw(self.frame * 25, self.action * 25, 25, 25, self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group == 'princess:gold':
            pass

from pico2d import*

import game_framework

# princess Run Speed
PIXEL_PER_METER = (250.0 / 10)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Floor:
    def __init__(self):
        self.x = 0
        self.size = 1000
        self.image = load_image('grass.png')
    def update(self):
        self.x += RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        self.image.clip_draw(0, 0, self.size, 60, self.size / 2 + 1200 - int(self.x), 40)

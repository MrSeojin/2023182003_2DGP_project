from pico2d import load_image

import game_framework

# princess Run Speed
PIXEL_PER_METER = (100.0 / 20)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Background:
    def __init__(self):
        self.image = load_image('map_background_snow.png')
        self.count = 0
        self.x = 0

    def update(self):
        self.x += RUN_SPEED_PPS * game_framework.frame_time
        if self.x >= 2000:
            self.x = 0

    def draw(self):
        if self.x > 800:
            self.image.clip_draw(int(self.x), 0, 2000 - int(self.x), 600, (2000 - int(self.x)) / 2, 300)
            self.image.clip_draw(0, 0, int(self.x) - 800, 600, 1200 - (int(self.x) - 800) / 2, 300)
        else:
            self.image.clip_draw(int(self.x), 0, 1200, 600, 600, 300)



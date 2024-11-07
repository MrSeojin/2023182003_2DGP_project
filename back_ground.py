from pico2d import load_image

class Background:
    def __init__(self):
        self.image = load_image('map_background.png')
        self.count = 0
        self.x = 0

    def update(self):
        if (self.count + 1) % 2 == 1 :
            self.x += 1
        if self.x >= 2000:
            self.x = 0

    def draw(self):
        if self.x > 800:
            self.image.clip_draw(self.x, 0, 2000 - self.x, 600, (2000 - self.x) / 2, 300)
            self.image.clip_draw(0, 0, self.x - 800, 600, 1200 - (self.x - 800) / 2, 300)
        else:
            self.image.clip_draw(self.x, 0, 1200, 600, 600, 300)



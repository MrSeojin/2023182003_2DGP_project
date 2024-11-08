from pico2d import*

class Floor:
    def __init__(self):
        self.x = 0
        self.size = 1000
        self.image = load_image('grass.png')
    def update(self):
        self.x += 1
    def draw(self):
        self.image.clip_draw(0, 0, self.size, 60, self.size / 2 + 1200 - self.x, 40)

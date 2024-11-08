from pico2d import*

class Gold:
    def __init__(self):
        self.x, self.y = 500, 300
        self.frame, self.action = 0, 0
        self.dir = 0
        self.image = load_image('coin.png')
    def update(self):
        self.frame = (self.frame + 1) % 4
    def draw(self):
        self.image.clip_draw(self.frame * 25, self.action * 25, 25, 25, self.x, self.y)

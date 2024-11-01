from pico2d import*
import random
from princess import*

class Page:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

class Gold:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

class Floor:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        else:
            princess.handle_event(event)

def reset_world():
    global running
    global world
    global princess
    running = True
    world = []
#    page = Page()
#    world.append(page)
    princess = Princess()
    world.append(princess)

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def main():
    open_canvas(1200, 600)
    reset_world()
    while running:
        handle_events()
        update_world()
        render_world()
        delay(0.05)
    close_canvas()

if __name__=='__main__':
    main()
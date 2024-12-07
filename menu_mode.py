import game_framework
from pico2d import*
from sdl2 import*

import game_world
from pannel import Pannel
import play_mode

def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel, 3)

def finish():
    game_world.remove_object(pannel)

def update():
    pass

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def handle_events(play_mode=None):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            pannel.handle_event(event)

def pause():
    pass

def resume():
    pass

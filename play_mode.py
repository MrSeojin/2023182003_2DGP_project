import game_framework
from pico2d import *

import game_world
import title_mode
from back_ground import Background
from princess import Princess
from mob import Mob

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            princess.handle_event(event)

def init():
    global world
    global princess
    global mob
    global background
    running = True
    world = []

    background = Background()
    game_world.add_object(background, 0)
    princess = Princess()
    game_world.add_object(princess, 1)
    mob = Mob()
    game_world.add_object(mob, 1)


def finish():
    game_world.clear()

def update():
    game_world.update()
    delay(0.04)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

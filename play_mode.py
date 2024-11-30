import game_framework
from pico2d import *
import random
import game_world
import title_mode
from back_ground import Background, Fever
from floor import Floor
from prince import Prince
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
    global background
    global mobs
    global floor
    global fever_time
    global score

    fever_time = False
    score = 0

    background = Background()
    game_world.add_object(background, 0)

    princess = Princess()
    game_world.add_object(princess, 2)

    mobs = []
    #mobs.append(Mob(random.randint(0,1200)))
    #game_world.add_objects(mobs, 2)

    floor = Floor(2000, 1200, 0)
    game_world.add_object(floor, 1)
    game_world.add_collision_pair('princess:floor', None, floor)
    game_world.add_collision_pair('mob:floor', None, floor)
    floor = Floor(800, 1200, random.randint(100, 400))
    game_world.add_object(floor, 1)
    game_world.add_collision_pair('princess:floor', None, floor)
    game_world.add_collision_pair('mob:floor', None, floor)

    game_world.add_collision_pair('princess:mob', princess, None)
    game_world.add_collision_pair('princess:floor', princess, None)

def finish():
    game_world.clear()

def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

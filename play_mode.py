import game_framework
from pico2d import *
import random
import game_world
import menu_mode
from back_ground import Background
from floor import Floor
from princess import Princess
from quest import Quest
from game_over import Score


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_mode(menu_mode)
        else:
            princess.handle_event(event)
            if princess.stop:
                total_score.handle_event(event)

def init():
    global world
    global princess
    global background
    global mobs
    global floor
    global fever_time
    global score
    global gold
    global distance
    global quest
    global total_score
    global bgm_play, sound_play

    bgm_play, sound_play = 'play','play'
    fever_time = False
    score = 0
    distance = 0
    gold = 0
    total_score = None

    quest = Quest()
    game_world.add_object(quest, 3)

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
    game_world.add_collision_pair('princess:gold', princess, None)
    game_world.add_collision_pair('princess:floor', princess, None)
    game_world.add_collision_pair('princess:fly_item', princess, None)
    game_world.add_collision_pair('princess:double_item', princess, None)

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
